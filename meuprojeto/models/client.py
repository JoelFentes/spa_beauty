from sqlalchemy import Column, Integer, String, Date
from .base import Base

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True, unique=True)
    telefone = Column(String(20), nullable=True)
    data_nascimento = Column(Date, nullable=True)
    observacoes = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Client(nome={self.nome}, email={self.email})>"
