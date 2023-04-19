from sqlalchemy import Column, Integer, String

from db.datebase import Base


class Candidato(Base):
    __tablename__ = "candidatos"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(100), nullable=False)
    email: str = Column(String(100), nullable=False)
    avatar_url: int = Column(String(255), nullable=False)
