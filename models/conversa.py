from sqlalchemy import Column, String
from database import Base

class Conversa(Base):
    __tablename__ = "conversas"

    telefone_whatsapp = Column(String, primary_key=True)
    estado = Column(String)
    orcamento_id = Column(String)
