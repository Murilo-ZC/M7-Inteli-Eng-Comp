# Ref: https://pythontic.com/pandas/serialization/postgresql
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Cria a instância da engine do banco de dados
alchemyEngine = create_engine('postgresql+psycopg2://postgres:senha@127.0.0.1', pool_recycle=3600);

# Conecta com o banco de dados
dbConnection = alchemyEngine.connect();

# Le os dados da tabela
dataFrame = pd.read_sql("select * from person", dbConnection);
print(dataFrame);

# Fecha a conexão com o banco de dados
dbConnection.close();

