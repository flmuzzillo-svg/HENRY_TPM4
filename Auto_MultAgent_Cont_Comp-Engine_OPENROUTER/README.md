# LegalMove (OpenRouter) — Agente Autónomo de Comparación de Contratos

Sistema multi-agente que procesa pares de imágenes escaneadas (contrato original + enmienda), extrae el texto mediante modelos de visión a través de **OpenRouter** y utiliza dos agentes LLM especializados para identificar, clasificar y reportar los cambios legales en un JSON estructurado y validado por **Pydantic**, con trazabilidad completa en **Langfuse**.

> **Nota:** Esta versión utiliza [OpenRouter](https://openrouter.ai/) como proveedor de API, lo que permite acceder a múltiples modelos (OpenAI, Anthropic, Google, etc.) con una sola API key.

---

## Arquitectura del Pipeline

```
Imágenes (JPG/PNG)
      │
      ▼
┌─────────────────────┐
│   image_parser.py   │  ← OpenRouter Vision (OCR legal de alta precisión)
│  parse_contract_    │
│      image()        │
└──────┬──────────────┘
       │  texto original + texto enmienda
       ▼
┌─────────────────────────────────────┐
│  contextualization_agent.py         │  ← Agente 1: El Auditor Legal
│  Mapea estructura del documento.    │    Chain-of-Thought + Few-Shot
│  NO extrae cambios, solo contexto.  │
└──────────────┬──────────────────────┘
               │  mapa estructural (markdown)
               ▼
┌─────────────────────────────────────┐
│  extraction_agent.py                │  ← Agente 2: El Analista de Compliance
│  Identifica, clasifica y describe   │    Few-Shot JSON + validación Pydantic
│  cada cambio detectado.             │
└──────────────┬──────────────────────┘
               │  ContractAnalysisResult (Pydantic)
               ▼
          JSON final validado
```

**Observabilidad Langfuse (Nativa / Idiomática):**
```
trace/generation: run_contract_analysis
  ├── span: parse_contract_image (original)
  │     └── generation: parse_original_contract (vía Langfuse OpenAI wrapper)
  ├── span: parse_contract_image (enmienda)
  │     └── generation: parse_amendment_contract (vía Langfuse OpenAI wrapper)
  ├── span: run_contextualization_agent
  │     └── generation: ChatOpenAI (vía CallbackHandler de Langchain)
  └── span: run_extraction_agent
        └── generation: ChatOpenAI (vía CallbackHandler de Langchain)
```

---

## Estructura del Repositorio

```
Auto_MultAgent_Cont_Comp-Engine_OPENROUTER/
├── src/
│   ├── __init__.py
│   ├── main.py                          # Orquestador del pipeline
│   ├── models.py                        # Esquemas Pydantic
│   ├── image_parser.py                  # GPT-4o Vision wrapper
│   └── agents/
│       ├── __init__.py
│       ├── contextualization_agent.py   # Agente 1 — El Auditor
│       └── extraction_agent.py          # Agente 2 — El Analista
├── data/
│   └── test_contracts/                  # 3 pares de imágenes de prueba
├── requirements.txt
├── .env.example
└── README.md
```

---

## Esquema de Output (Pydantic)

```python
class ContractChangeOutput(BaseModel):
    clause_affected: str           # Ej: "Cláusula 3.2 — Confidencialidad"
    original_text: str             # Texto en el contrato original
    modified_text: str             # Texto en la enmienda
    change_type: Literal["Suma", "Resta", "Modificación"]
    legal_impact_level: Literal["Alto", "Medio", "Bajo"]
    sections_changed: List[str]    # Ej: ["3", "3.2"]
    topics_touched: List[str]      # Ej: ["Confidencialidad", "Plazo"]
    summary_of_the_change: str     # Descripción narrativa del cambio

class ContractAnalysisResult(BaseModel):
    total_changes: int
    overall_risk_assessment: Literal["Alto", "Medio", "Bajo"]
    changes: List[ContractChangeOutput]
```

---

## Instalación y Configuración

### 1. Clonar el repositorio y crear el entorno virtual

```bash
git clone <URL_DEL_REPO>
cd Auto_MultAgent_Cont_Comp-Engine_OPENROUTER
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

```bash
copy .env.example .env        # Windows
# cp .env.example .env        # Linux / macOS
```

Completar el archivo `.env` con las claves reales:

| Variable | Descripción | Dónde obtenerla |
|----------|-------------|-----------------|
| `OPENROUTER_API_KEY` | API Key de OpenRouter | [openrouter.ai/keys](https://openrouter.ai/keys) |
| `LANGFUSE_PUBLIC_KEY` | Clave pública de Langfuse | [cloud.langfuse.com → Settings → API Keys](https://cloud.langfuse.com) |
| `LANGFUSE_SECRET_KEY` | Clave secreta de Langfuse | Mismo lugar |
| `LLM_MODEL` | Modelo para los agentes de texto | `openai/gpt-4o` o `openai/gpt-4o-mini` |
| `VISION_MODEL` | Modelo para el parsing de imágenes | `openai/gpt-4o` (recomendado) |

### 4. Agregar imágenes de contratos

Colocar los pares de imágenes en `data/test_contracts/` con el siguiente naming convention:

```
data/test_contracts/
├── documento_1__original.jpg
├── documento_1__enmienda.jpg
├── documento_2__original.jpg
└── documento_2__enmienda.jpg
```

---

## Ejecución

```bash
# Desde la raíz del proyecto
python src/main.py
```

El sistema procesará todos los pares de contratos en `data/test_contracts/` y mostrará el JSON de análisis en la consola. Los traces completos estarán disponibles en el dashboard de Langfuse.

### Ejemplo de output

```json
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
      "summary_of_the_change": "Se incrementa el honorario mensual de USD 5.000 a USD 7.500 (aumento del 50%)."
    }
  ]
}
```

---

## Variables de Entorno

| Variable | Valor por defecto | Descripción |
|----------|------------------|-------------|
| `OPENROUTER_API_KEY` | — | Requerida. API Key de OpenRouter. |
| `LANGFUSE_PUBLIC_KEY` | — | Requerida. Clave pública de Langfuse. |
| `LANGFUSE_SECRET_KEY` | — | Requerida. Clave secreta de Langfuse. |
| `LANGFUSE_HOST` | `https://cloud.langfuse.com` | Host de Langfuse (self-hosted opcional). |
| `LLM_MODEL` | `openai/gpt-4o` | Modelo para agentes de texto (formato: `proveedor/modelo`). |
| `VISION_MODEL` | `openai/gpt-4o` | Modelo para parsing de imágenes (formato: `proveedor/modelo`). |

---

## Stack Técnico

| Tecnología | Versión | Rol |
|-----------|---------|-----|
| Python | 3.10+ | Lenguaje base |
| OpenRouter API | — | Gateway multi-modelo (OpenAI, Anthropic, Google) |
| LangChain | 0.3.x | Orquestación de agentes |
| Pydantic | 2.x | Validación estricta de esquemas |
| Langfuse | 2.x | Observabilidad y trazabilidad |
| python-dotenv | 1.x | Gestión de variables de entorno |

---

## Rúbrica de Evaluación

| Criterio | Peso | Implementación |
|----------|------|----------------|
| Parsing Multimodal | 15% | `image_parser.py` con prompt OCR especializado y `detail: high` |
| Arquitectura de Agentes | 15% | Separación Auditor / Analista con responsabilidades únicas |
| Validación Pydantic | 10% | `ContractAnalysisResult` + `ContractChangeOutput` con `strict=True` |
| Calidad del Prompting | 15% | Chain-of-Thought (Ag.1) + Few-Shot JSON (Ag.2) + delimitadores XML |
| Gestión de Errores | 10% | `try-except` en cada llamada API con logging en Langfuse |
| Observabilidad | 15% | Trace raíz + 4 spans hijos con inputs, outputs y latencia |
| Calidad de Código | 10% | Docstrings, type hints, principios SOLID, modularidad |
| Defensa Técnica | 10% | Demo en vivo con los 3 pares de contratos de prueba |
