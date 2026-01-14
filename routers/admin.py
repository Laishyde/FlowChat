from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.orcamento import Orcamento

router = APIRouter(prefix="/admin")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/orcamentos")
def listar_orcamentos(db: Session = Depends(get_db)):
    return db.query(Orcamento).all()
