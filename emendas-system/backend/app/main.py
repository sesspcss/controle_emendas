from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/emendas/")
def criar_emenda(emenda: schemas.EmendaCreate, db: Session = Depends(database.get_db)):
    return crud.criar_emenda(db, emenda)

@app.get("/emendas/")
def listar_emendas(db: Session = Depends(database.get_db)):
    return crud.listar_emendas(db)

@app.post("/usuarios/")
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(database.get_db)):
    return crud.criar_usuario(db, usuario)

@app.get("/usuarios/")
def listar_usuarios(db: Session = Depends(database.get_db)):
    return crud.listar_usuarios(db)

