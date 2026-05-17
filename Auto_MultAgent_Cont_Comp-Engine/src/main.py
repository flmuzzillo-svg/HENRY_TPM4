"""
main.py
-------
Orquestador principal del pipeline LegalMove.

Ejecuta el flujo completo de análisis de contratos:
  1. Carga del par de imágenes (original + enmienda).
  2. Parsing multimodal con GPT-4o Vision (image_parser).
  3. Agente 1 — Contextualización estructural (ContextualizationAgent).
  4. Agente 2 — Extracción y clasificación de cambios (ExtractionAgent).
  5. Validación Pydantic y output del JSON final.

Toda la ejecución está instrumentada con Langfuse bajo una jerarquía
de trace → spans para trazabilidad completa.
"""

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from langfuse import Langfuse

# Asegurar que src/ esté en el path para imports relativos
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.image_parser import parse_contract_image
from src.agents.contextualization_agent import run_contextualization_agent
from src.agents.extraction_agent import run_extraction_agent
from src.models import ContractAnalysisResult

# ---------------------------------------------------------------------------
# Configuración del entorno
# ---------------------------------------------------------------------------
load_dotenv()

LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY", "")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY", "")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

# ---------------------------------------------------------------------------
# Inicialización de Langfuse
# ---------------------------------------------------------------------------
langfuse = Langfuse(
    public_key=LANGFUSE_PUBLIC_KEY,
    secret_key=LANGFUSE_SECRET_KEY,
    host=LANGFUSE_HOST,
)


# ---------------------------------------------------------------------------
# Función principal del pipeline
# ---------------------------------------------------------------------------

def run_contract_analysis(
    original_image_path: str | Path,
    amendment_image_path: str | Path,
    pair_label: str = "documento",
) -> ContractAnalysisResult:
    """
    Ejecuta el pipeline completo de análisis de contratos.

    Pipeline:
        Imágenes → Parsing Vision → Agente 1 → Agente 2 → JSON validado

    Args:
        original_image_path:  Ruta a la imagen del contrato original.
        amendment_image_path: Ruta a la imagen de la enmienda.
        pair_label:           Identificador del par de contratos para Langfuse
                              (ej: 'documento_1').

    Returns:
        ContractAnalysisResult validado por Pydantic.

    Raises:
        FileNotFoundError: Si alguna de las imágenes no existe.
        RuntimeError:      Si algún paso del pipeline falla.
    """
    original_path = Path(original_image_path)
    amendment_path = Path(amendment_image_path)

    # Validación temprana de rutas
    if not original_path.exists():
        raise FileNotFoundError(f"Contrato original no encontrado: {original_path}")
    if not amendment_path.exists():
        raise FileNotFoundError(f"Enmienda no encontrada: {amendment_path}")

    print(f"\n{'='*60}")
    print(f"  Iniciando análisis: {pair_label}")
    print(f"  Original : {original_path.name}")
    print(f"  Enmienda : {amendment_path.name}")
    print(f"{'='*60}\n")

    # ------------------------------------------------------------------
    # Crear trace raíz en Langfuse
    # ------------------------------------------------------------------
    trace = langfuse.trace(
        name="contract-analysis",
        input={
            "pair_label": pair_label,
            "original": str(original_path.resolve()),
            "amendment": str(amendment_path.resolve()),
        },
        tags=["legalmove", "contract-comparison"],
    )

    try:
        # --------------------------------------------------------------
        # PASO 1 & 2: Parsing multimodal de ambas imágenes
        # --------------------------------------------------------------
        print("[1/4] Parseando imagen del contrato original...")
        original_text = parse_contract_image(
            image_path=original_path,
            document_label="parse_original_contract",
            langfuse_trace=trace,
        )
        print(f"      ✓ Extraídos {len(original_text)} caracteres del original.\n")

        print("[2/4] Parseando imagen de la enmienda...")
        amendment_text = parse_contract_image(
            image_path=amendment_path,
            document_label="parse_amendment_contract",
            langfuse_trace=trace,
        )
        print(f"      ✓ Extraídos {len(amendment_text)} caracteres de la enmienda.\n")

        # --------------------------------------------------------------
        # PASO 3: Agente 1 — Contextualización
        # --------------------------------------------------------------
        print("[3/4] Ejecutando Agente 1 — Auditor Legal (contextualización)...")
        context_map = run_contextualization_agent(
            original_text=original_text,
            amendment_text=amendment_text,
            langfuse_trace=trace,
        )
        print(f"      ✓ Mapa de correspondencias generado ({len(context_map)} caracteres).\n")

        # --------------------------------------------------------------
        # PASO 4: Agente 2 — Extracción y validación Pydantic
        # --------------------------------------------------------------
        print("[4/4] Ejecutando Agente 2 — Analista de Compliance (extracción)...")
        analysis_result = run_extraction_agent(
            original_text=original_text,
            amendment_text=amendment_text,
            context_map=context_map,
            langfuse_trace=trace,
        )
        print(f"      ✓ {analysis_result.total_changes} cambio(s) identificado(s). "
              f"Riesgo global: {analysis_result.overall_risk_assessment}.\n")

        # Registrar resultado final en el trace de Langfuse
        trace.update(
            output={
                "total_changes": analysis_result.total_changes,
                "overall_risk_assessment": analysis_result.overall_risk_assessment,
                "clauses_affected": [
                    c.clause_affected for c in analysis_result.changes
                ],
            },
        )

        return analysis_result

    except Exception as exc:
        # Registrar el error en el trace antes de propagar
        trace.update(
            output={"error": str(exc)},
            metadata={"status": "failed"},
        )
        raise


# ---------------------------------------------------------------------------
# Entry Point — Ejecuta todos los pares de contratos de prueba
# ---------------------------------------------------------------------------

def main():
    """
    Ejecuta el pipeline para todos los pares de contratos disponibles
    en el directorio data/test_contracts/.
    """
    # Directorio base del proyecto (un nivel arriba de src/)
    project_root = Path(__file__).parent.parent
    contracts_dir = project_root / "data" / "test_contracts"

    if not contracts_dir.exists():
        print(f"ERROR: No se encontró el directorio de contratos: {contracts_dir}")
        sys.exit(1)

    # Detectar pares automáticamente (documento_N__original + documento_N__enmienda)
    originals = sorted(contracts_dir.glob("*__original.*"))

    if not originals:
        print(f"ERROR: No se encontraron imágenes originales en {contracts_dir}")
        sys.exit(1)

    all_results = []

    for original_path in originals:
        # Construir la ruta esperada de la enmienda
        pair_name = original_path.stem.replace("__original", "")
        ext = original_path.suffix

        amendment_path = contracts_dir / f"{pair_name}__enmienda{ext}"

        if not amendment_path.exists():
            print(f"  ⚠ Enmienda no encontrada para '{original_path.name}', saltando.\n")
            continue

        try:
            result = run_contract_analysis(
                original_image_path=original_path,
                amendment_image_path=amendment_path,
                pair_label=pair_name,
            )

            # Serializar resultado como JSON con indentación
            result_json = result.model_dump()
            all_results.append({pair_name: result_json})

            print(f"{'─'*60}")
            print(f"  RESULTADO — {pair_name}")
            print(f"{'─'*60}")
            print(json.dumps(result_json, ensure_ascii=False, indent=2))
            print()

        except Exception as exc:
            print(f"\n  ✗ Error procesando '{pair_name}': {exc}\n")

    # Flush de Langfuse para asegurar que todos los eventos se envíen
    langfuse.flush()

    print(f"\n{'='*60}")
    print(f"  Pipeline finalizado. {len(all_results)} par(es) procesado(s).")
    print(f"  Revisá los traces en: {LANGFUSE_HOST}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
