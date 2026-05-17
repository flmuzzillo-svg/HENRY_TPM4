"""
models.py
---------
Esquemas de validación Pydantic para el sistema LegalMove.

Define los modelos de datos que estructuran la salida del pipeline
de comparación de contratos. Utiliza Pydantic v2 con configuración
estricta para garantizar la integridad de los datos.
"""

from typing import List, Literal
from pydantic import BaseModel, Field, ConfigDict


class ContractChangeOutput(BaseModel):
    """
    Representa un cambio individual detectado entre el contrato
    original y su enmienda.

    Campos requeridos por la consigna técnica del proyecto LegalMove.
    """

    model_config = ConfigDict(strict=True)

    # --- Identificación de la cláusula ---
    clause_affected: str = Field(
        ...,
        description="Número o nombre de la cláusula afectada (ej: 'Cláusula 3.2 - Confidencialidad').",
    )

    # --- Textos comparados ---
    original_text: str = Field(
        ...,
        description="Fragmento exacto del texto en el contrato original.",
    )
    modified_text: str = Field(
        ...,
        description="Fragmento exacto del texto en la enmienda. Vacío si el cambio es una eliminación.",
    )

    # --- Clasificación del cambio ---
    change_type: Literal["Suma", "Resta", "Modificación"] = Field(
        ...,
        description=(
            "Tipo de cambio aplicado: "
            "'Suma' (texto agregado), "
            "'Resta' (texto eliminado), "
            "'Modificación' (texto reemplazado)."
        ),
    )

    # --- Impacto legal ---
    legal_impact_level: Literal["Alto", "Medio", "Bajo"] = Field(
        ...,
        description=(
            "Nivel de impacto legal estimado por el Agente Analista: "
            "'Alto' (afecta obligaciones principales o derechos fundamentales), "
            "'Medio' (afecta condiciones secundarias o plazos), "
            "'Bajo' (cambios formales o de redacción sin impacto sustantivo)."
        ),
    )

    # --- Campos de síntesis (requeridos por la consigna) ---
    sections_changed: List[str] = Field(
        ...,
        description="Lista de identificadores de secciones modificadas (ej: ['3', '3.2', '5.1']).",
    )
    topics_touched: List[str] = Field(
        ...,
        description=(
            "Categorías legales o comerciales afectadas por el cambio "
            "(ej: ['Confidencialidad', 'Plazo', 'Penalidades'])."
        ),
    )
    summary_of_the_change: str = Field(
        ...,
        description="Descripción narrativa clara y detallada del cambio identificado.",
    )


class ContractAnalysisResult(BaseModel):
    """
    Contenedor raíz del análisis completo de un par de contratos.

    Agrupa todos los cambios detectados entre el contrato original
    y su enmienda en una sola estructura validada.
    """

    model_config = ConfigDict(strict=True)

    total_changes: int = Field(
        ...,
        description="Número total de cambios detectados en el análisis.",
    )
    changes: List[ContractChangeOutput] = Field(
        ...,
        description="Lista ordenada de todos los cambios identificados.",
    )
    overall_risk_assessment: Literal["Alto", "Medio", "Bajo"] = Field(
        ...,
        description=(
            "Evaluación de riesgo global del conjunto de cambios. "
            "Se determina por el nivel de impacto más alto presente en la lista."
        ),
    )
