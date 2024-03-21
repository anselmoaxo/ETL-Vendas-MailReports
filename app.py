import yaml

# Carrega as configurações do arquivo YAML
with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Acessa as configurações do Gmail e do banco de dados
gmail_config = config['gmail']
database_config = config['database']

# Use as configurações conforme necessário
print(gmail_config['email'])
print(database_config['dialect'])