from sqlalchemy import Column, Integer, String, UniqueConstraint

from db.datebase import Base


class Candidato(Base):
    __tablename__ = "candidatos"

    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String(100), nullable=False)
    nome: str = Column(String(100), nullable=False)
    idade: int = Column(Integer, nullable=False)
    sobre: str = Column(String(510), nullable=False)
    avatar_url: str = Column(String(255), nullable=True)
