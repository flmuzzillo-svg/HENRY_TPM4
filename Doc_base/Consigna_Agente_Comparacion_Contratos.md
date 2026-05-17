# Proyecto: Agente Autónomo de Comparación de Contratos (LegalMove)

## 1. Contexto y Objetivos
Imagina que trabajas como **AI Engineer** en una empresa de tecnología legal (**LegalMove**) que procesa miles de enmiendas de contratos cada mes.

Actualmente, el equipo de Compliance (Cumplimiento Legal) pasa más de 40 horas a la semana comparando manualmente los contratos originales con sus enmiendas (adendas) para identificar qué cambió, evaluar el impacto legal y derivar los documentos para su revisión. Este proceso manual es lento, propenso a errores humanos y un cuello de botella para escalar el negocio.

**Misión:** Construir un Agente Autónomo de Comparación de Contratos. El sistema recibirá imágenes escaneadas, las leerá utilizando IA de visión y utilizará un equipo de "analistas virtuales" (Agentes de IA) para extraer exactamente qué cláusulas se modificaron, devolviendo un reporte estructurado (JSON) y validado.

### 🎯 Objetivo Principal
Desarrollar un sistema multi-agente autónomo que:
1.  Extraiga texto de imágenes escaneadas mediante modelos multimodales (Visión).
2.  Identifique, extraiga y resuma cambios legales mediante la colaboración de dos agentes especializados.
3.  Garantice trazabilidad completa mediante Langfuse y validación estricta con Pydantic.

---

## 2. Stack Técnico
* **OpenAI GPT-4o (Vision):** Para el parseo de imágenes a texto estructurado.
* **LangChain:** Para la orquestación de agentes.
* **Pydantic:** Para validación de esquemas de salida.
* **Langfuse:** Para observabilidad y trazado (tracing) del workflow.
* **Python + python-dotenv:** Lenguaje base y gestión de entorno.

---

## 3. Consigna Técnica (Etapas del Proyecto)

### Paso 1: Parsing Multimodal de Imágenes
Implementar `parse_contract_image()`:
* Recibe el path de una imagen (JPEG/PNG).
* Codifica en base64.
* Llama a la API de GPT-4o Vision para extraer el texto completo de forma fiel.
* **Registro:** Cada ejecución debe registrarse en Langfuse (inputs, outputs, latencia, tokens).

### Paso 2: Agente 1 - Contextualización (`ContextualizationAgent`)
* **Responsabilidad:** Recibir los dos textos parseados y producir un mapa de estructura comparada.
* **Output:** Texto estructurado que identifique correspondencias entre secciones y el propósito de cada bloque. No extrae cambios, solo construye el contexto.

### Paso 3: Agente 2 - Extracción de Cambios (`ExtractionAgent`)
* **Responsabilidad:** Recibir el mapa contextual y los textos para identificar, aislar y describir cada cambio (adiciones, eliminaciones, modificaciones).
* **Output:** JSON estructurado listo para validación.

### Paso 4: Validación con Pydantic
Definir el modelo `ContractChangeOutput`:
* `sections_changed`: List[str] (Identificadores de secciones).
* `topics_touched`: List[str] (Categorías legales/comerciales).
* `summary_of_the_change`: str (Descripción detallada).

### Paso 5: Trazabilidad con Langfuse
Instrumentar el pipeline con una estructura jerárquica:
* `contract-analysis` (Raíz)
    * `parse_original_contract`
    * `parse_amendment_contract`
    * `contextualization_agent`
    * `extraction_agent`

---

## 4. Entregables y Estructura del Repositorio

| Archivo | Descripción |
| :--- | :--- |
| `src/main.py` | Entry point que ejecuta el pipeline completo. |
| `src/agents/contextualization_agent.py` | Lógica y system prompt del Agente 1. |
| `src/agents/extraction_agent.py` | Lógica y system prompt del Agente 2. |
| `src/image_parser.py` | Funciones de encoding y llamadas a Vision API. |
| `src/models.py` | Modelos Pydantic (ContractChangeOutput). |
| `data/test_contracts/` | Mínimo 2 pares de contratos (4 imágenes). |
| `README.md` | Documentación, diagramas y guía de uso. |
| `requirements.txt` | Dependencias con versiones fijas. |

---

## 5. Rúbrica de Evaluación

| Criterio | Peso | Descripción |
| :--- | :---: | :--- |
| **Parsing Multimodal** | 15% | Precisión en la extracción y respeto de jerarquías. |
| **Arquitectura de Agentes** | 15% | Separación clara de responsabilidades y flujo lógico. |
| **Validación Pydantic** | 10% | Uso estricto de esquemas y manejo de excepciones. |
| **Calidad del Prompting** | 15% | System prompts especializados (Senior vs Auditor). |
| **Gestión de Errores** | 10% | Robustez ante fallos de API y gestión de `.env`. |
| **Observabilidad** | 15% | Jerarquía de spans en Langfuse y registro de métricas. |
| **Calidad de Código** | 10% | Modularidad, limpieza y documentación del README. |
| **Defensa Técnica** | 10% | Explicación fluida y demo exitosa en vivo. |

---

## 6. Recursos Adicionales
* **OpenAI Vision Docs:** [Images and vision](https://platform.openai.com/docs/guides/vision)
* **Langfuse Setup:** [cloud.langfuse.com](https://cloud.langfuse.com)
