from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.sqlite import BLOB
from datetime import datetime
import uuid

from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String)
    telefone_whatsapp = Column(String, unique=True)
    email = Column(String)
    empresa = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
