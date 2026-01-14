from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from datetime import datetime
import uuid

from database import Base

class Orcamento(Base):
    __tablename__ = "orcamentos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    protocolo = Column(String, unique=True)
    status = Column(String)
    prazo_desejado = Column(String)
    observacoes = Column(String)
    valor_total = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    cliente_id = Column(String, ForeignKey("clientes.id"))
