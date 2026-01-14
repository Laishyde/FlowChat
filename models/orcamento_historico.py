from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
import uuid

from database import Base

class OrcamentoHistorico(Base):
    __tablename__ = "orcamento_historico"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    orcamento_id = Column(String, ForeignKey("orcamentos.id"))
    status = Column(String)
    descricao = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
