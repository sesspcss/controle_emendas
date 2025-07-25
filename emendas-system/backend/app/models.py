from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Emenda(Base):
    __tablename__ = "emendas"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, index=True)
    parlamentar = Column(String)
    valor = Column(String)
    destino = Column(String)
    descricao = Column(Text)
    status = Column(String, default="Pendente")
    responsavel_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    responsavel = relationship("Usuario", back_populates="emendas")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    tipo = Column(String, default="analista")  