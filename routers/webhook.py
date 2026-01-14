from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.conversa import Conversa
from models.orcamento import Orcamento
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/webhook")
async def webhook(request: Request, db: Session = Depends(get_db)):
    try:
        data = await request.json()

        telefone = data.get("telefone")
        mensagem = data.get("mensagem")

        if not telefone or not mensagem:
            return {
                "erro": "Payload inválido",
                "esperado": {
                    "telefone": "string",
                    "mensagem": "string"
                }
            }

        conversa = db.query(Conversa).filter_by(
            telefone_whatsapp=telefone
        ).first()

        if not conversa:
            conversa = Conversa(
                telefone_whatsapp=telefone,
                estado="aguardando_produto"
            )
            db.add(conversa)
            db.commit()
            return {"resposta": "Olá! Qual produto você deseja?"}

        if conversa.estado == "aguardando_produto":
            conversa.estado = "aguardando_quantidade"
            db.commit()
            return {"resposta": "Qual a quantidade?"}

        if conversa.estado == "aguardando_quantidade":
            conversa.estado = "aguardando_prazo"
            db.commit()
            return {"resposta": "Qual o prazo desejado?"}

        if conversa.estado == "aguardando_prazo":
            conversa.estado = "finalizado"
            db.commit()
            return {"resposta": "Perfeito! Seu pedido foi enviado para análise."}

        return {"resposta": "Fluxo finalizado"}

    except Exception as e:
        print("❌ ERRO:", e)
        return {"erro": "Erro interno", "detail": str(e)}
