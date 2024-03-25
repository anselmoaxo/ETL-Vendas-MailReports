from src.utils.configuracao import carregar_config
from src.extract.db_extractor import extract_data, caminho_sql
from src.transform.data_formatter import transform_vendas
from src.load.email_sender import enviar_email

config = carregar_config()
email_1 = config['gmail']['email']
senha = config['gmail']['password']
    
destinatario = 'aoliveira@cstecnologia.com.br'
assunto = 'Analise Ultimas Vendas'
corpo = 'Segue analise dos cliente com mais de 30 dias sem retornar a compra'
caminho_do_anexo = ['data/output/vendas.xlsx',
                    'data/output/ranking_produto_2020.xlsx',
                    'data/output/ranking_produto_2021.xlsx',
                    'data/output/ranking_produto_2022.xlsx',
                    'data/output/ranking_produto_2023.xlsx']
                    
print(caminho_do_anexo)
if __name__ == "__main__":
    sql_query = caminho_sql()   
    df_vendas = extract_data(sql_query)
    df_vendas = transform_vendas(df_vendas)
    enviar_email(email_1, senha, destinatario, assunto, 
                 corpo, caminho_do_anexo)