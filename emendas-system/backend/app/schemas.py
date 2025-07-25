from pydantic import BaseModel
from typing import Optional

class EmendaBase(BaseModel):
    numero: str
    parlamentar: str
    valor: str
    destino: str
    descricao: Optional[str] = None
    status: Optional[str] = "Pendente"
    responsavel_id: Optional[int] = None

class EmendaCreate(EmendaBase):
    pass

class Emenda(EmendaBase):
    id: int

    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nome: str
    email: str

class UsuarioCreate(UsuarioBase):
    senha: str
    tipo: Optional[str] = "analista"

class Usuario(UsuarioBase):
    id: int
    tipo: str

    class Config:
        orm_mode = True

