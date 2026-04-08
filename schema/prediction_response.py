from pydantic import BaseModel,Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str= Field(
        ...,
        description='Predicted insurance premium category',
        example='High'
    )
    confidence_score: float = Field(
        ...,
        description=" Model's confidence on the predicted class",
        example=0.85
    )

    other_probabilities:Dict[str,float]= Field(
        ...,
        description='Probability distrbution across all the classes'
    )