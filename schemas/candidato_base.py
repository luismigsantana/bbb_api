from pydantic import BaseModel, Field
from typing import Optional


class CandidatoBase(BaseModel):
    nome: str
    email: str
    sobre: str
    idade: int
    avatar_url: Optional[str] = Field(None)
