from sqlalchemy import Column, String, Boolean, DateTime, Float
from datetime import datetime
import uuid

from database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String)
    descricao = Column(String)
    preco_base = Column(Float)
    ativo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
