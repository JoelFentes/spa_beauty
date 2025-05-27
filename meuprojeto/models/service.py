from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))
    imagem = Column(String(100))
    duracao_minutos = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Service(nome={self.nome}, preco={self.preco})>"
