# Script utilizado para criar as tabelas no banco de dados
# Utilizado apenas no momento da criação do banco de dados

# Importações utilizadas
from shared.base import Base, engine
from shared.tables import Cotacao

if __name__=="__main__":
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(engine)