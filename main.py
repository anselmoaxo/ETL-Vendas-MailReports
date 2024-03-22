import pandas as pd
import os
from src.utils.create_email import EmailSender
import yaml
from src.extract.db_extractor import extract_data
from src.transform.data_formatter import transform_vendas



with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)
    
database_config = config['gmail']
email_1 = config['gmail']['email']
senha = config['gmail']['password']


# Obtendo o caminho absoluto do diretório raiz do projeto
root_dir = os.path.dirname(os.path.abspath(__file__))

# Concatenando o caminho do arquivo vendas.sql com o caminho absoluto do diretório raiz do projeto
file_path = os.path.join(root_dir, 'data', 'input', 'venda.sql')
if os.path.exists(file_path):
    # Agora você pode usar o arquivo
    with open(file_path, 'r') as file:
        sql_query = file.read()
        # Faça o que precisar com o conteúdo do arquivo
else:
    print("O arquivo não foi encontrado:", file_path)
    
df_vendas = extract_data(sql_query)
df_vendas = transform_vendas(df_vendas)
df_vendas.to_excel('data/output/vendas.xlsx', index=False)


email_sender = EmailSender(email_1, senha)
destinatario = 'aoliveira@cstecnologia.com.br'
assunto = 'Analise Ultimas Vendas'
corpo = 'Segue analise dos cliente com mais de 30 dias sem retornar a compra'

    # Substitua 'caminho/do/anexo' pelo caminho do arquivo que você deseja anexar
caminho_do_anexo = 'data/output/vendas.xlsx'

email_sender.send_email(destinatario, assunto, corpo, caminho_do_anexo)
