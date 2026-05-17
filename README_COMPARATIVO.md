# LegalMove — Comparativa: OpenAI vs OpenRouter

Este repositorio contiene **dos implementaciones** del mismo sistema multi-agente de comparación de contratos, cada una conectada a un proveedor de API diferente. Ambas comparten la misma arquitectura, lógica de agentes y esquemas Pydantic.

---

## Resumen de Versiones

| Característica | `Auto_MultAgent_Cont_Comp-Engine` | `Auto_MultAgent_Cont_Comp-Engine_OPENROUTER` |
|----------------|:---------------------------------:|:--------------------------------------------:|
| **Proveedor API** | OpenAI directo | OpenRouter (gateway) |
| **Variable de API Key** | `OPENAI_API_KEY` | `OPENROUTER_API_KEY` |
| **Formato de modelo** | `gpt-4o` | `openai/gpt-4o` |
| **Base URL** | `https://api.openai.com/v1` (default) | `https://openrouter.ai/api/v1` |
| **Modelos disponibles** | Solo OpenAI | OpenAI, Anthropic, Google, Meta, Mistral, etc. |
| **Requiere cuenta en** | [platform.openai.com](https://platform.openai.com) | [openrouter.ai](https://openrouter.ai) |

---

## Arquitectura Común

Ambas versiones comparten exactamente el mismo pipeline:

```
Imágenes (JPG/PNG)
      │
      ▼
┌─────────────────────┐
│   image_parser.py   │  ← Vision API (OCR legal)
└──────┬──────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│  contextualization_agent.py         │  ← Agente 1: Auditor Legal
│  (Chain-of-Thought + Few-Shot)      │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  extraction_agent.py                │  ← Agente 2: Analista de Compliance
│  (Few-Shot JSON + Pydantic)         │
└──────────────┬──────────────────────┘
               │
               ▼
          JSON validado (Pydantic)
```

**Observabilidad (Langfuse):**
Ambas versiones están 100% instrumentadas de manera **idéntica** e **idiomática** utilizando la última especificación del SDK de Langfuse (v2), evitando instrumentación manual innecesaria:

* **Trazabilidad Global (`@observe`):** Se utiliza el decorador `@observe` en el orquestador principal (`run_contract_analysis`) y en los agentes/parsers para registrar automáticamente la estructura jerárquica.
* **Integración Langchain (`CallbackHandler`):** Los agentes LLM (`ChatOpenAI`) envían sus métricas internas de tokens, prompts y latencia automáticamente a través del callback nativo de LangChain (`CallbackHandler`).
* **Wrapper de OpenAI (`langfuse.openai`):** La extracción OCR Vision se realiza con el wrapper nativo de Langfuse, que calcula automáticamente los tokens de imágenes y latencia del modelo de visión.

#### Jerarquía de Spans en Langfuse
```
trace/generation: run_contract_analysis (Orquestador principal)
  ├── span: parse_contract_image (original)
  │     └── generation: parse_original_contract (OCR Vision)
  ├── span: parse_contract_image (enmienda)
  │     └── generation: parse_amendment_contract (OCR Vision)
  ├── span: run_contextualization_agent (Agente 1)
  │     └── generation: ChatOpenAI (LangChain flow)
  └── span: run_extraction_agent (Agente 2)
        └── generation: ChatOpenAI (LangChain flow)
```

---

## Diferencias Técnicas en el Código

### 1. Cliente de Vision (`image_parser.py`)

**OpenAI directo:**
```python
_openai_client = OpenAI(api_key=OPENAI_API_KEY)
```

**OpenRouter:**
```python
_openai_client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)
```

### 2. Agentes LangChain (`contextualization_agent.py` / `extraction_agent.py`)

**OpenAI directo:**
```python
llm = ChatOpenAI(model="gpt-4o", temperature=0)
```

**OpenRouter:**
```python
llm = ChatOpenAI(
    model="openai/gpt-4o",
    temperature=0,
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
)
```

### 3. Variables de entorno (`.env`)

**OpenAI directo:**
```env
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4o
VISION_MODEL=gpt-4o
```

**OpenRouter:**
```env
OPENROUTER_API_KEY=sk-or-v1-...
LLM_MODEL=openai/gpt-4o
VISION_MODEL=openai/gpt-4o
```

---

## Pros y Contras

### ✅ OpenAI Directo (`Auto_MultAgent_Cont_Comp-Engine`)

| Pros | Contras |
|------|---------|
| 🟢 Conexión directa sin intermediarios — menor latencia teórica | 🔴 Limitado a modelos de OpenAI exclusivamente |
| 🟢 Configuración más simple (menos parámetros) | 🔴 Requiere cuenta y créditos en OpenAI |
| 🟢 Acceso inmediato a las últimas versiones de modelos OpenAI | 🔴 Sin fallback si la API de OpenAI tiene problemas |
| 🟢 Documentación oficial extensa y soporte directo | 🔴 Precios fijos de OpenAI, sin posibilidad de comparar costos |
| 🟢 Garantía de compatibilidad total con el SDK de OpenAI | 🔴 Vendor lock-in: migrar a otro proveedor requiere reescribir código |

### ✅ OpenRouter (`Auto_MultAgent_Cont_Comp-Engine_OPENROUTER`)

| Pros | Contras |
|------|---------|
| 🟢 Acceso a +200 modelos de múltiples proveedores con una sola API key | 🔴 Capa adicional de red — latencia ligeramente mayor |
| 🟢 Cambiar de modelo es solo editar el `.env` (sin tocar código) | 🔴 Dependencia de un servicio intermediario (OpenRouter) |
| 🟢 Posibilidad de comparar costos entre proveedores en tiempo real | 🔴 Disponibilidad sujeta al uptime de OpenRouter + proveedor final |
| 🟢 Créditos gratuitos para modelos seleccionados | 🔴 Algunos modelos tienen limitaciones vs. la API nativa |
| 🟢 Ideal para prototipado rápido y experimentación multi-modelo | 🔴 La facturación tiene un markup sobre el precio base del proveedor |
| 🟢 Sin vendor lock-in: migrar entre modelos sin cambios de código | 🔴 Features avanzadas de cada proveedor pueden no estar expuestas |

---

## Cuándo Usar Cada Versión

```
                    ┌─────────────────────┐
                    │  ¿Qué necesitás?    │
                    └─────────┬───────────┘
                              │
                 ┌────────────┴────────────┐
                 │ ¿Solo modelos de OpenAI?│
                 └────────────┬────────────┘
                    Sí /             \ No
                      /               \
        ┌────────────┴──────┐    ┌─────┴──────────────────┐
        │ ¿Producción con   │    │  ➜ OpenRouter           │
        │   SLA estricto?   │    │  (acceso multi-modelo)  │
        └────────┬──────────┘    └─────────────────────────┘
           Sí /       \ No
             /         \
  ┌─────────┴────┐  ┌───┴──────────────────────┐
  │ ➜ OpenAI     │  │ ¿Querés comparar modelos │
  │   Directo    │  │    fácilmente?            │
  └──────────────┘  └──────────┬───────────────┘
                         Sí /       \ No
                           /         \
             ┌────────────┴───┐  ┌────┴─────────┐
             │ ➜ OpenRouter   │  │ ➜ OpenAI     │
             │                │  │   Directo    │
             └────────────────┘  └──────────────┘
```

| Escenario | Recomendación |
|-----------|---------------|
| Producción empresarial con SLA | **OpenAI Directo** — menor latencia, sin intermediarios |
| Prototipado y experimentación | **OpenRouter** — probar distintos modelos sin cambiar código |
| Presupuesto limitado | **OpenRouter** — acceso a modelos gratuitos y comparación de precios |
| Proyecto académico / entrega | **Cualquiera** — ambos cumplen los requisitos de la consigna |
| Necesidad de modelos no-OpenAI | **OpenRouter** — acceso a Claude, Gemini, Llama, Mistral, etc. |

---

## Estructura del Repositorio

```
HENRY_TPM4/
├── Auto_MultAgent_Cont_Comp-Engine/           ← Versión OpenAI directo
│   ├── src/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── image_parser.py
│   │   └── agents/
│   │       ├── contextualization_agent.py
│   │       └── extraction_agent.py
│   ├── data/test_contracts/
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── Auto_MultAgent_Cont_Comp-Engine_OPENROUTER/ ← Versión OpenRouter
│   ├── src/                                     (misma estructura)
│   ├── data/test_contracts/
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── Doc_base/                                    ← Documentación y contratos de ejemplo
├── Consigna_Agente_Comparacion_Contratos.md
├── Prompt_maestro_tpm4.md
└── README_COMPARATIVO.md                        ← Este archivo
```

---

## Ejecución Rápida

### OpenAI Directo
```bash
cd Auto_MultAgent_Cont_Comp-Engine
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # Completar OPENAI_API_KEY
python src/main.py
```

### OpenRouter
```bash
cd Auto_MultAgent_Cont_Comp-Engine_OPENROUTER
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # Completar OPENROUTER_API_KEY
python src/main.py
```

> Ambas versiones producen el mismo JSON de salida validado por Pydantic y registran las trazas en Langfuse con idéntica jerarquía de spans.
