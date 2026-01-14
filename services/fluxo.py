from sqlalchemy.orm import Session
from database import SessionLocal
from models.conversa import Conversa

def processar_mensagem(telefone: str, mensagem: str):
    db: Session = SessionLocal()

    conversa = db.query(Conversa).filter_by(telefone=telefone).first()

    # 1️⃣ PRIMEIRO CONTATO
    if not conversa:
        conversa = Conversa(
            telefone=telefone,
            estado="PEDINDO_PRODUTO"
        )
        db.add(conversa)
        db.commit()
        return (
            "Olá! 👋\n"
            "Vamos montar seu orçamento.\n\n"
            "Qual produto você deseja?"
        )

    # 2️⃣ PRODUTO
    if conversa.estado == "PEDINDO_PRODUTO":
        conversa.estado = "PEDINDO_QUANTIDADE"
        db.commit()
        return "Perfeito! Qual a quantidade desejada?"

    # 3️⃣ QUANTIDADE
    if conversa.estado == "PEDINDO_QUANTIDADE":
        conversa.estado = "PEDINDO_PRAZO"
        db.commit()
        return "Qual o prazo desejado?"

    # 4️⃣ PRAZO
    if conversa.estado == "PEDINDO_PRAZO":
        conversa.estado = "AGUARDANDO_APROVACAO"
        db.commit()
        return (
            "🧾 *Orçamento gerado!*\n\n"
            "Digite:\n"
            "1️⃣ Aprovar orçamento\n"
            "2️⃣ Rejeitar orçamento"
        )

    # 5️⃣ APROVAÇÃO
    if conversa.estado == "AGUARDANDO_APROVACAO":
        if mensagem == "1":
            conversa.estado = "ORCAMENTO_APROVADO"
            db.commit()
            return "✅ Orçamento aprovado! Nossa equipe entrará em contato."

        if mensagem == "2":
            conversa.estado = "ORCAMENTO_REJEITADO"
            db.commit()
            return "❌ Orçamento rejeitado. Se quiser alterar algo, é só avisar."

        return (
            "Por favor, responda com:\n"
            "1️⃣ Aprovar\n"
            "2️⃣ Rejeitar"
        )

    # fallback
    return "Posso te ajudar com algo mais?"
