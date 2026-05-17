"""
contextualization_agent.py
--------------------------
Agente 1 — El Auditor Legal.

Responsabilidad ÚNICA: recibir los dos textos extraídos (contrato original
y enmienda) y construir un mapa estructurado de correspondencias entre
secciones. NO extrae cambios — solo contextualiza la estructura para
que el Agente 2 pueda trabajar con precisión.

Técnica de prompting: Chain-of-Thought con delimitadores XML-style y
role de Auditor Senior.
"""

import os
import time

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langfuse import observe

# ---------------------------------------------------------------------------
# Configuración del entorno
# ---------------------------------------------------------------------------
load_dotenv()

LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o")

# ---------------------------------------------------------------------------
# System Prompt del Auditor (Agente 1)
# ---------------------------------------------------------------------------
AUDITOR_SYSTEM_PROMPT = """Eres un Auditor Legal Senior con 20 años de experiencia \
en derecho contractual corporativo. Tienes una habilidad excepcional para \
diseccionar documentos legales complejos y mapear su estructura interna.

TU MISIÓN EN ESTE PASO:
Construir un mapa detallado de correspondencia estructural entre el contrato \
original y su enmienda. Tu output alimentará al Agente Analista que luego \
identificará los cambios exactos.

PROCESO DE RAZONAMIENTO (Chain-of-Thought):
Paso 1 — Lee el contrato ORIGINAL e identifica todas sus secciones y cláusulas.
Paso 2 — Lee la ENMIENDA e identifica todas sus secciones y cláusulas.
Paso 3 — Mapea qué sección de la enmienda corresponde a qué sección del original.
Paso 4 — Para cada sección mapeada, describe brevemente su propósito legal.
Paso 5 — Identifica si hay secciones que aparecen SOLO en uno de los dos documentos.

REGLAS ESTRICTAS:
- NO extraigas ni menciones cambios específicos entre textos. Eso es tarea del Agente 2.
- NO parafrasees el contenido legal. Solo mapea la estructura.
- Usa el formato de output indicado sin desviarte.

FORMATO DE OUTPUT REQUERIDO:
## MAPA DE CORRESPONDENCIA ESTRUCTURAL

### Secciones del Contrato Original
[Lista numerada de todas las secciones identificadas con su propósito]

### Secciones de la Enmienda
[Lista numerada de todas las secciones identificadas con su propósito]

### Tabla de Correspondencias
| Sección Original | Sección Enmienda | Propósito Legal | Estado |
|-----------------|-----------------|-----------------|--------|
[Filas: Estado puede ser: CORRESPONDE / SOLO_EN_ORIGINAL / SOLO_EN_ENMIENDA]

### Observaciones del Auditor
[Notas relevantes sobre la estructura que el Agente 2 debe considerar]"""

# Ejemplo few-shot (incluido en el prompt de usuario para guiar el formato)
FEW_SHOT_EXAMPLE = """
EJEMPLO DE OUTPUT ESPERADO:
## MAPA DE CORRESPONDENCIA ESTRUCTURAL

### Secciones del Contrato Original
1. Cláusula 1 — Objeto del Contrato: Define el servicio de consultoría prestado.
2. Cláusula 2 — Plazo: Establece la duración del acuerdo (12 meses).
3. Cláusula 3 — Honorarios: Fija los montos y condiciones de pago.

### Secciones de la Enmienda
1. Cláusula 1 — Objeto del Contrato: Define el servicio de consultoría prestado.
2. Cláusula 2 — Plazo: Establece la duración del acuerdo.
3. Cláusula 3 — Honorarios: Fija los montos y condiciones de pago.
4. Cláusula 4 — Penalidades: Nueva cláusula sobre incumplimientos.

### Tabla de Correspondencias
| Sección Original     | Sección Enmienda      | Propósito Legal              | Estado              |
|---------------------|-----------------------|------------------------------|---------------------|
| Cláusula 1          | Cláusula 1            | Objeto del contrato          | CORRESPONDE         |
| Cláusula 2          | Cláusula 2            | Plazo de vigencia            | CORRESPONDE         |
| Cláusula 3          | Cláusula 3            | Condiciones económicas       | CORRESPONDE         |
| —                   | Cláusula 4            | Régimen de penalidades       | SOLO_EN_ENMIENDA    |

### Observaciones del Auditor
- La Cláusula 4 es completamente nueva y no tiene equivalente en el original.
- El texto de la Cláusula 2 parece haber sido modificado en duración.
"""


# ---------------------------------------------------------------------------
# Función principal del agente
# ---------------------------------------------------------------------------

@observe(as_type="span")
def run_contextualization_agent(
    original_text: str,
    amendment_text: str,
    callbacks: list = None,
) -> str:
    """
    Ejecuta el Agente 1 (Auditor) para construir el mapa estructural
    de correspondencias entre el contrato original y su enmienda.

    Args:
        original_text:   Texto extraído del contrato original por image_parser.
        amendment_text:  Texto extraído de la enmienda por image_parser.
        callbacks:       Lista de callbacks de Langchain (ej: Langfuse CallbackHandler).

    Returns:
        Mapa estructural en formato markdown (string).

    Raises:
        RuntimeError: Si la llamada al LLM falla.
    """
    llm = ChatOpenAI(model=LLM_MODEL, temperature=0)

    # Construir el mensaje de usuario con delimitadores XML-style
    user_content = f"""{FEW_SHOT_EXAMPLE}

---
Ahora analiza los siguientes documentos reales:

<ORIGINAL>
{original_text}
</ORIGINAL>

<ENMIENDA>
{amendment_text}
</ENMIENDA>

Aplica tu proceso de razonamiento paso a paso y genera el MAPA DE CORRESPONDENCIA ESTRUCTURAL."""

    messages = [
        SystemMessage(content=AUDITOR_SYSTEM_PROMPT),
        HumanMessage(content=user_content),
    ]

    try:
        response = llm.invoke(
            messages,
            config={"callbacks": callbacks} if callbacks else None
        )
        context_map: str = response.content

        return context_map

    except Exception as exc:
        error_msg = f"Error en ContextualizationAgent: {exc}"
        raise RuntimeError(error_msg) from exc
