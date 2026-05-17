# PROMPT DE DESARROLLO: SISTEMA MULTI-AGENTE LEGALMOVE

## ROL
Actúa como un **Senior AI Engineer & Solutions Architect** experto en orquestación de agentes, modelos multimodales (Visión) y observabilidad. Tu objetivo es codificar el sistema "LegalMove" siguiendo estrictamente la estructura y objetivos definidos en la consigna del proyecto.

## CONTEXTO Y MISIÓN
Debes construir un Agente Autónomo de Comparación de Contratos que procese imágenes de contratos originales y sus enmiendas. El sistema debe extraer texto mediante GPT-4o Vision y utilizar dos agentes especializados para identificar cambios legales, entregando un JSON estructurado y validado.

## STACK TÉCNICO REQUERIDO
- **Orquestación:** LangChain.
- **Modelos:** OpenAI GPT-4o (con capacidades de Visión).
- **Validación:** Pydantic (Estricta).
- **Observabilidad:** Langfuse (Implementación de trazas y spans).
- **Entorno:** Python 3.10+, gestión de variables de entorno con `.env`.

## ESTRUCTURA DE ARCHIVOS A GENERAR
Por favor, desarrolla el código completo para los siguientes módulos:

1. `src/models.py`:
   - Define el esquema `ContractChangeOutput` usando Pydantic. 
   - Debe incluir campos para: cláusula afectada, texto original, texto modificado, tipo de cambio (Suma, Resta, Modificación) y nivel de impacto legal.

2. `src/image_parser.py`:
   - Implementa funciones de encoding base64 para imágenes.
   - Crea el wrapper para llamar a la API de Visión de GPT-4o, asegurando un parseo preciso del texto jerárquico del contrato.

3. `src/agents/contextualization_agent.py` (Agente 1 - El Auditor):
   - **System Prompt:** Define un rol de Auditor Legal meticuloso. Su tarea es comparar los textos extraídos e identificar discrepancias exactas.
   - Implementa la lógica de razonamiento (Chain-of-Thought) antes de pasar la información al siguiente agente.

4. `src/agents/extraction_agent.py` (Agente 2 - El Analista):
   - **System Prompt:** Define un rol de Especialista en Cumplimiento (Compliance). Su tarea es tomar las discrepancias identificadas y estructurarlas en el modelo Pydantic definido.
   - Debe evaluar el impacto legal de cada cambio identificado.

5. `main.py`:
   - El orquestador principal que ejecuta el pipeline: Carga de imágenes -> Parsing -> Agente 1 -> Agente 2 -> Output Final.
   - Implementa la integración con **Langfuse** para garantizar la trazabilidad de cada paso del proceso mediante decoradores o callbacks de LangChain.

6. `requirements.txt` y `.env.example`:
   - Incluye todas las dependencias con versiones fijas y las variables necesarias (OPENAI_API_KEY, LANGFUSE_PUBLIC_KEY, etc.).

## REQUISITOS DE CALIDAD Y VALIDACIÓN
- **Modularidad:** El código debe ser limpio, comentado y seguir principios SOLID.
- **Gestión de Errores:** Implementa bloques try-except robustos para fallos de API o parsing de imágenes.
- **Prompting:** Aplica técnicas de "Few-Shot" y delimitadores claros en los System Prompts de los agentes para maximizar la precisión.
- **Validación:** Asegura que la salida final sea exclusivamente el objeto JSON validado por Pydantic.

## INSTRUCCIÓN FINAL
Genera el código de cada archivo de manera secuencial, asegurando que las importaciones entre módulos sean correctas según la estructura de carpetas `src/`. Comienza ahora con la implementación de `src/models.py`.