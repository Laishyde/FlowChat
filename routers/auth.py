from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.usuario import Usuario
from core.security import hash_senha, criar_token

router = APIRouter(prefix="/auth")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(dados: dict, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter_by(
        email=dados["email"],
        senha=hash_senha(dados["senha"])
    ).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="Login inválido")

    return {
        "access_token": criar_token({"sub": usuario.email}),
        "perfil": usuario.perfil,
        "nome": usuario.nome
    }
