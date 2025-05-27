from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from .base import Base

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    funcionario_id = Column(Integer, ForeignKey('funcionarios.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    data_hora = Column(DateTime, nullable=False)
    status = Column(String(20), default='agendado')  # agendado, concluído, cancelado

    client = relationship("Client")
    funcionario = relationship("Funcionario")
    service = relationship("Service")

    def __repr__(self):
        return f"<Appointment(cliente={self.client_id}, servico={self.service_id}, data={self.data_hora})>"
