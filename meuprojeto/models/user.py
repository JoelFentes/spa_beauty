from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), default='admin')  # admin, recepcionista etc.

    def __repr__(self):
        return f"<User(username={self.username}, role={self.role})>"
