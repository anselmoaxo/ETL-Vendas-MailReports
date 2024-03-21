import pandas as pd
from scripts import conexao
from dotenv import load_dotenv
import os
from scripts.create_email import EmailSender

load_dotenv()
senha = os.getenv("SENHA")
email_1 = os.getenv("EMAIL")

engine = conexao.engine
# Obtendo o caminho absoluto do diretório raiz do projeto
root_dir = os.path.dirname(os.path.abspath(__file__))

# Concatenando o caminho do arquivo vendas.sql com o caminho absoluto do diretório raiz do projeto
file_path = os.path.join(root_dir, 'data', 'venda.sql')
if os.path.exists(file_path):
    # Agora você pode usar o arquivo
    with open(file_path, 'r') as file:
        sql_query = file.read()
        # Faça o que precisar com o conteúdo do arquivo
else:
    print("O arquivo não foi encontrado:", file_path)
    
df_vendas = pd.read_sql(sql_query, engine)

df_vendas = df_vendas[['nfe01_000_nota', 'nfe01_013_demi','nfe01_332_vprod',
                                'nfe01_000_cliente', 'nfe01_000_gerafaturamento']]

df_vendas = df_vendas.rename(columns={
     'nfe01_000_nota': 'nota',
    'nfe01_013_demi': 'data_emissao',
    'nfe01_332_vprod': 'valor',
    'nfe01_000_cliente': 'cliente',
    'nfe01_000_gerafaturamento': 'gerafaturamento'
}).sort_values(by=['data_emissao', 'nota'], ascending=False).reset_index()

condicao = df_vendas['cliente'] > 0

df_vendas = df_vendas[condicao]

df_vendas = (df_vendas.groupby(['cliente']).agg({'nota': 'count',
                                                  'valor': 'sum',
                                                  'data_emissao': 'max'}).rename(
                                            columns={
                                                    'nota' :' qtd_notas',
                                                    'valor': 'valor_total',
                                                    'data_emissao': 'ultima_dt_compra'
                                                      }
                                                  ).reset_index()
)
df_vendas = df_vendas.sort_values(by='ultima_dt_compra', ascending=False)
df_vendas.to_excel('data/vendas.xlsx', index=False)


email_sender = EmailSender(email_1, senha)
destinatario = 'aoliveira@cstecnologia.com.br'
assunto = 'Analise Ultimas Vendas'
corpo = 'Segue analise dos cliente com mais de 30 dias sem retornar a compra'

    # Substitua 'caminho/do/anexo' pelo caminho do arquivo que você deseja anexar
caminho_do_anexo = 'data/vendas.xlsx'

email_sender.send_email(destinatario, assunto, corpo, caminho_do_anexo)
