import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List

from models.candidatos import Candidato
from db.datebase import engine, Base, get_db
from repositories.CandidatoRepo import CandidatoRepository
from schemas.candidato_request import CandidatoRequest
from schemas.candidato_response import CandidatoResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/api/candidatos", response_model=CandidatoResponse, status_code=status.HTTP_201_CREATED)
def create(request: CandidatoRequest, db: Session = Depends(get_db)):
    candidato = CandidatoRepository.save(db, Candidato(**request.dict()))
    return CandidatoResponse.from_orm(candidato)


@app.get("/api/candidatos", response_model=List[CandidatoResponse])
def find_all(db: Session = Depends(get_db)):
    candidatos = CandidatoRepository.find_all(db)
    return [CandidatoResponse.from_orm(candidato) for candidato in candidatos]


@app.get("/api/candidatos/{id}", response_model=CandidatoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    candidato = CandidatoRepository.find_by_id(db, id)
    if not candidato:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Candidato não encontrado"
        )
    return CandidatoResponse.from_orm(candidato)


@app.delete("/api/candidatos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not CandidatoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Candidato não encontrado"
        )
    CandidatoRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/api/candidatos/{id}", response_model=CandidatoResponse)
def update(id: int, request: CandidatoRequest, db: Session = Depends(get_db)):
    if not CandidatoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Candidato não encontrado"
        )
    candidato = CandidatoRepository.save(db, Candidato(id=id, **request.dict()))
    return CandidatoResponse.from_orm(candidato)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)