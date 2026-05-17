"""
extraction_agent.py
-------------------
Agente 2 — El Analista de Compliance.

Responsabilidad ÚNICA: recibir el mapa contextual generado por el Agente 1
(El Auditor) y los textos originales para identificar, aislar y clasificar
cada cambio legal. Produce el JSON estructurado validado por Pydantic.

Técnica de prompting: Few-Shot con ejemplo JSON completo + delimitadores
XML-style para separar los inputs.
"""

import json
import os
import time

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import ValidationError

from src.models import ContractAnalysisResult

# ---------------------------------------------------------------------------
# Configuración del entorno
# ---------------------------------------------------------------------------
load_dotenv()

LLM_MODEL: str = os.getenv("LLM_MODEL", "openai/gpt-4o")
OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

# ---------------------------------------------------------------------------
# System Prompt del Analista (Agente 2)
# ---------------------------------------------------------------------------
ANALYST_SYSTEM_PROMPT = """Eres un Especialista en Compliance Legal con \
certificación internacional en análisis de contratos corporativos.

TU MISIÓN:
Recibir el mapa estructural generado por el Auditor Legal (Agente 1) junto \
con los textos completos del contrato original y su enmienda. Debes identificar \
EXACTAMENTE qué texto cambió en cada cláusula y producir un reporte JSON \
estructurado y preciso.

PROCESO DE ANÁLISIS:
1. Para cada correspondencia en el mapa del Auditor, compara los textos exactos.
2. Si detectas una diferencia, clasifícala: Suma / Resta / Modificación.
3. Evalúa el impacto legal: Alto / Medio / Bajo.
4. Extrae las categorías legales afectadas (topics_touched).
5. Escribe un resumen claro del cambio en lenguaje natural.

CLASIFICACIÓN DE IMPACTO:
- Alto:  Afecta obligaciones principales, montos, plazos críticos o derechos fundamentales.
- Medio: Afecta condiciones secundarias, procedimientos o plazos no críticos.
- Bajo:  Cambios formales, de redacción, puntuación o estilo sin impacto sustantivo.

REGLA CRÍTICA:
Responde EXCLUSIVAMENTE con un objeto JSON válido. No incluyas texto antes \
ni después del JSON. No uses bloques de código markdown. Solo el JSON puro."""

# ---------------------------------------------------------------------------
# Few-Shot Example (incluido en el mensaje de usuario)
# ---------------------------------------------------------------------------
FEW_SHOT_JSON_EXAMPLE = """
EJEMPLO DE OUTPUT JSON ESPERADO:
{
  "total_changes": 2,
  "overall_risk_assessment": "Alto",
  "changes": [
    {
      "clause_affected": "Cláusula 3.1 — Honorarios Mensuales",
      "original_text": "El cliente abonará la suma de USD 5.000 mensuales.",
      "modified_text": "El cliente abonará la suma de USD 7.500 mensuales.",
      "change_type": "Modificación",
      "legal_impact_level": "Alto",
      "sections_changed": ["3", "3.1"],
      "topics_touched": ["Honorarios", "Obligaciones Económicas"],
      "summary_of_the_change": "Se incrementa el honorario mensual de USD 5.000 a USD 7.500, representando un aumento del 50% en la obligación económica principal del cliente."
    },
    {
      "clause_affected": "Cláusula 4 — Penalidades por Incumplimiento",
      "original_text": "",
      "modified_text": "En caso de incumplimiento de pago, se aplicará un interés punitorio del 3% mensual sobre el saldo adeudado.",
      "change_type": "Suma",
      "legal_impact_level": "Alto",
      "sections_changed": ["4"],
      "topics_touched": ["Penalidades", "Incumplimiento", "Intereses"],
      "summary_of_the_change": "Se incorpora una nueva cláusula de penalidades que establece un interés punitorio del 3% mensual ante mora en el pago. Esta cláusula no existía en el contrato original."
    }
  ]
}
"""


# ---------------------------------------------------------------------------
# Función principal del agente
# ---------------------------------------------------------------------------

def run_extraction_agent(
    original_text: str,
    amendment_text: str,
    context_map: str,
    langfuse_trace=None,
) -> ContractAnalysisResult:
    """
    Ejecuta el Agente 2 (Analista) para extraer y clasificar los cambios
    entre el contrato original y su enmienda.

    Args:
        original_text:   Texto extraído del contrato original.
        amendment_text:  Texto extraído de la enmienda.
        context_map:     Mapa estructural generado por el Agente 1 (Auditor).
        langfuse_trace:  Objeto trace de Langfuse (opcional).

    Returns:
        ContractAnalysisResult validado por Pydantic.

    Raises:
        RuntimeError: Si la llamada al LLM falla o el JSON no puede validarse.
    """
    llm = ChatOpenAI(
        model=LLM_MODEL,
        temperature=0,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
    )

    # Construir el mensaje de usuario con delimitadores XML-style
    user_content = f"""{FEW_SHOT_JSON_EXAMPLE}

---
Ahora analiza los siguientes documentos reales:

<CONTEXTO_AUDITOR>
{context_map}
</CONTEXTO_AUDITOR>

<ORIGINAL>
{original_text}
</ORIGINAL>

<ENMIENDA>
{amendment_text}
</ENMIENDA>

Genera el JSON de análisis de cambios. Recuerda: responde SOLO con el JSON puro, \
sin ningún texto adicional ni bloques de código markdown."""

    messages = [
        SystemMessage(content=ANALYST_SYSTEM_PROMPT),
        HumanMessage(content=user_content),
    ]

    # Crear span en Langfuse si hay un trace activo
    span = None
    if langfuse_trace is not None:
        span = langfuse_trace.span(
            name="extraction_agent",
            input={
                "context_map_preview": context_map[:300] + "...",
                "original_text_preview": original_text[:200] + "...",
                "amendment_text_preview": amendment_text[:200] + "...",
                "model": LLM_MODEL,
            },
        )

    start_time = time.time()

    try:
        response = llm.invoke(messages)
        elapsed_ms = int((time.time() - start_time) * 1000)
        raw_json: str = response.content.strip()

        # Limpiar posibles bloques markdown que el modelo pudiera agregar
        if raw_json.startswith("```"):
            raw_json = raw_json.split("```")[1]
            if raw_json.startswith("json"):
                raw_json = raw_json[4:]
            raw_json = raw_json.strip()

        # Parsear y validar con Pydantic
        try:
            parsed_data = json.loads(raw_json)
            result = ContractAnalysisResult.model_validate(parsed_data)
        except (json.JSONDecodeError, ValidationError) as val_err:
            error_msg = (
                f"Fallo en la validación Pydantic del output del Agente 2. "
                f"JSON recibido:\n{raw_json}\n\nError: {val_err}"
            )
            if span is not None:
                span.end(
                    output={"error": error_msg, "raw_json": raw_json[:500]},
                    metadata={"latency_ms": elapsed_ms, "status": "validation_error"},
                    level="ERROR",
                )
            raise RuntimeError(error_msg) from val_err

        if span is not None:
            span.end(
                output={
                    "total_changes": result.total_changes,
                    "overall_risk": result.overall_risk_assessment,
                    "changes_preview": [
                        c.clause_affected for c in result.changes
                    ],
                },
                metadata={
                    "latency_ms": elapsed_ms,
                    "model": LLM_MODEL,
                    "validation": "pydantic_ok",
                },
            )

        return result

    except RuntimeError:
        raise  # Re-lanzar errores ya formateados (incluyendo validación)

    except Exception as exc:
        elapsed_ms = int((time.time() - start_time) * 1000)
        error_msg = f"Error en ExtractionAgent: {exc}"

        if span is not None:
            span.end(
                output={"error": error_msg},
                metadata={"latency_ms": elapsed_ms, "status": "error"},
                level="ERROR",
            )

        raise RuntimeError(error_msg) from exc
