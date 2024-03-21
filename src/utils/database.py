import sqlalchemy as sa
import psycopg2
import yaml
from sqlalchemy.exc import SQLAlchemyError

# Carrega as configurações do arquivo YAML
with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Acessa as configurações do Gmail e do banco de dados
database_config = config['database']
dialect = config['database']['dialect']
host = config['database']['host']
port = config['database']['port']
username = config['database']['username']
password = config['database']['password']
database_name = config['database']['database_name']

# Use as configurações conforme necessário
database_url = f'{dialect}+psycopg2://{username}:{password}@{host}:{port}/{database_name}'

engine = sa.create_engine(database_url, poolclass=sa.pool.QueuePool, max_overflow=10)

try:
    # Tenta conectar ao banco de dados
    connection = engine.connect()
    print("Conexão bem-sucedida!")
    # Faça o que precisar com a conexão
except SQLAlchemyError as e:
    # Se ocorrer um erro ao conectar
    print("Erro ao conectar ao banco de dados:", e)
finally:
    # Fecha a conexão
    if connection:
        connection.close()
