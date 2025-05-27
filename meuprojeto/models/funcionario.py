from sqlalchemy import Column, Integer, String
from .base import Base

class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cargo = Column(String(50))  # Ex: cabeleireiro, manicure
    telefone = Column(String(20))
    email = Column(String(100), unique=True)

    def __repr__(self):
        return f"<Funcionario(nome={self.nome}, cargo={self.cargo})>"
