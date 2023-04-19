from sqlalchemy.orm import Session

from models.candidatos import Candidato


class CandidatoRepository:
    @staticmethod
    def find_all(db: Session):
        return db.query(Candidato).all()

    @staticmethod
    def save(db: Session, candidato: Candidato) -> Candidato:
        if candidato.id:
            db.merge(candidato)
        else:
            db.add(candidato)
        db.commit()
        return candidato

    @staticmethod
    def find_by_id(db: Session, id: int) -> Candidato:
        return db.query(Candidato).filter(Candidato.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Candidato).filter(Candidato.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        candidato = db.query(Candidato).filter(Candidato.id == id).first()
        if candidato is not None:
            db.delete(candidato)
            db.commit()
