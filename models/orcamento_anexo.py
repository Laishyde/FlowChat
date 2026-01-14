from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
import uuid

from database import Base

class OrcamentoAnexo(Base):
    __tablename__ = "orcamento_anexos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    orcamento_id = Column(String, ForeignKey("orcamentos.id"))
    arquivo_url = Column(String)
    tipo = Column(String)  # imagem, pdf, doc
    created_at = Column(DateTime, default=datetime.utcnow)
