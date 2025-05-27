from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    valor = Column(Float, nullable=False)
    metodo = Column(String(50))  # Ex: dinheiro, cartão, pix
    data_pagamento = Column(DateTime, default=datetime.utcnow)

    appointment = relationship("Appointment")

    def __repr__(self):
        return f"<Payment(appointment_id={self.appointment_id}, valor={self.valor}, metodo={self.metodo})>"
