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

@router.post("/cadastro")
def cadastro(dados: dict, db: Session = Depends(get_db)):
    if db.query(Usuario).filter_by(email=dados["email"]).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    usuario = Usuario(
        nome=dados["nome"],
        email=dados["email"],
        senha=hash_senha(dados["senha"]),
        perfil="admin"
    )

    db.add(usuario)
    db.commit()

    return {"msg": "Usuário cadastrado"}

@router.post("/login")
def login(dados: dict, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter_by(
        email=dados["email"],
        senha=hash_senha(dados["senha"])
    ).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="Login inválido")

    return {"access_token": criar_token({"sub": usuario.email})}


