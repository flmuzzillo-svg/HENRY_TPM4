"""
image_parser.py
---------------
Módulo de parsing multimodal de imágenes de contratos.

Responsabilidades:
  - Codificar imágenes locales en base64.
  - Llamar a la API de GPT-4o Vision para extraer texto preservando
    la jerarquía legal del documento (secciones, cláusulas, párrafos).
  - Registrar cada llamada como un span en Langfuse (inputs, outputs, latencia).
"""

import base64
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from langfuse.openai import OpenAI
from langfuse import observe

# ---------------------------------------------------------------------------
# Configuración del entorno
# ---------------------------------------------------------------------------
load_dotenv()

VISION_MODEL: str = os.getenv("VISION_MODEL", "openai/gpt-4o")
OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

# Cliente OpenAI reutilizable (apuntando a OpenRouter)
_openai_client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
)

# ---------------------------------------------------------------------------
# System Prompt de Visión
# ---------------------------------------------------------------------------
VISION_SYSTEM_PROMPT = """Eres un sistema de OCR legal de alta precisión.
Tu tarea es transcribir FIELMENTE el texto contenido en la imagen de un contrato legal.

REGLAS ESTRICTAS:
1. Preserva la jerarquía exacta del documento: números de sección, letras de inciso,
   sangría y formato de sub-cláusulas.
2. Transcribe TODO el texto visible, sin resumir, omitir ni parafrasear.
3. Si encuentras texto en tablas, represéntalas con separadores de columna (|).
4. Si una palabra es ilegible, escribe [ILEGIBLE].
5. No añadas comentarios ni explicaciones propias.
6. Responde únicamente con el texto transcrito del documento."""


# ---------------------------------------------------------------------------
# Funciones públicas
# ---------------------------------------------------------------------------

def encode_image_to_base64(image_path: str | Path) -> str:
    """
    Codifica una imagen local en una cadena base64.

    Args:
        image_path: Ruta absoluta o relativa a la imagen (JPEG / PNG).

    Returns:
        String base64 de la imagen.

    Raises:
        FileNotFoundError: Si el archivo no existe en la ruta indicada.
        ValueError: Si la extensión del archivo no es soportada.
    """
    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"Imagen no encontrada: {path.resolve()}")

    supported_extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
    if path.suffix.lower() not in supported_extensions:
        raise ValueError(
            f"Formato no soportado: '{path.suffix}'. "
            f"Formatos válidos: {supported_extensions}"
        )

    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


@observe(as_type="span")
def parse_contract_image(
    image_path: str | Path,
    document_label: str = "contrato",
) -> str:
    """
    Extrae el texto completo de una imagen de contrato usando GPT-4o Vision.

    Preserva la estructura jerárquica del documento legal.

    Args:
        image_path:      Ruta a la imagen del contrato.
        document_label:  Etiqueta descriptiva para el span de Langfuse
                         (ej: 'parse_original_contract').

    Returns:
        Texto completo extraído del contrato como string.

    Raises:
        FileNotFoundError: Si la imagen no existe.
        RuntimeError: Si la llamada a la API de OpenAI falla.
    """
    path = Path(image_path)

    # Determinar el media type según la extensión
    ext = path.suffix.lower()
    media_type_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }
    media_type = media_type_map.get(ext, "image/jpeg")

    # Codificar imagen
    image_b64 = encode_image_to_base64(path)

    try:
        response = _openai_client.chat.completions.create(
            name=document_label,
            model=VISION_MODEL,
            messages=[
                {"role": "system", "content": VISION_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Por favor, transcribe fielmente todo el texto "
                                "de este documento legal, preservando su estructura jerárquica."
                            ),
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{media_type};base64,{image_b64}",
                                "detail": "high",
                            },
                        },
                    ],
                },
            ],
            max_tokens=4096,
        )

        extracted_text: str = response.choices[0].message.content or ""
        return extracted_text

    except Exception as exc:
        error_msg = f"Error en parse_contract_image para '{path.name}': {exc}"
        raise RuntimeError(error_msg) from exc
