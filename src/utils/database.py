import psycopg2
import yaml


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


