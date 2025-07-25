from sqlalchemy.orm import Session
from . import models, schemas

def criar_emenda(db: Session, emenda: schemas.EmendaCreate):
    db_emenda = models.Emenda(**emenda.dict())
    db.add(db_emenda)
    db.commit()
    db.refresh(db_emenda)
    return db_emenda

def listar_emendas(db: Session):
    return db.query(models.Emenda).all()

def criar_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def listar_usuarios(db: Session):
    return db.query(models.Usuario).all()

