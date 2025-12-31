from typing import List, Dict
from pydantic import BaseModel


class EvaluateRequest(BaseModel):
    reference_answer: str
    reference_concepts: List[str]
    student_answer: str
    preset: str              # "LATIHAN" | "UJIAN"


class EvaluateResponse(BaseModel):
    status: str
    final_score: float
    semantic: float
    coverage: float
    missing: List[str]
