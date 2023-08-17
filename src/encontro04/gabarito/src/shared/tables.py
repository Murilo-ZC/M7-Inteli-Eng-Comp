# Scripts com os modelos das tabelas

# Importações utilizadas
from sqlalchemy import Column, Integer, String, Float, DateTime
from shared.base import Base

class Cotacao(Base):
    """
    Classe que representa a tabela de cotações
    """
    __tablename__ = "cotacoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime)
    cotacao_compra = Column(Float)
    cotacao_venda = Column(Float)

    def __repr__(self):
        return f"<Cotacao(data={self.data}, cotacao_compra={self.cotacao_compra}, cotacao_venda={self.cotacao_venda})>"