from schemas.candidato_base import CandidatoBase


class CandidatoResponse(CandidatoBase):
    id: int

    class Config:
        orm_mode = True
