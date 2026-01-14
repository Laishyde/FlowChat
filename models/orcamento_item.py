from sqlalchemy import Column, String, Integer, Float, ForeignKey
from datetime import datetime
import uuid

from database import Base

class OrcamentoItem(Base):
    __tablename__ = "orcamento_itens"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    orcamento_id = Column(String, ForeignKey("orcamentos.id"))
    produto_id = Column(String, ForeignKey("produtos.id"))

    quantidade = Column(Integer)
    valor_unitario = Column(Float)
    valor_total = Column(Float)
