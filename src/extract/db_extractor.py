from sqlalchemy import create_engine
import pandas as pd
from ..utils.database import database_url
import os

engine = create_engine(database_url)


def caminho_sql():
    root_dir = os.getcwd()
    file_path = os.path.join(root_dir, 'data', 'input', 'venda.sql')
    if os.path.exists(file_path):
        # Agora você pode usar o arquivo
        with open(file_path, 'r') as file:
            sql_query = file.read()
            # Faça o que precisar com o conteúdo do arquivo
    else:
        print("O arquivo não foi encontrado:", file_path)
    return sql_query


def caminho_sql_ranking():
    root_dir = os.getcwd()
    file_path = os.path.join(root_dir, 'data', 'input', 'ranking_produto.sql')
    if os.path.exists(file_path):
        # Agora você pode usar o arquivo
        with open(file_path, 'r') as file:
            sql_ranking = file.read()
            # Faça o que precisar com o conteúdo do arquivo
    else:
        print("O arquivo não foi encontrado:", file_path)
    return sql_ranking


def extract_data(sql_query):
    df_vendas = pd.read_sql(sql_query, engine)
    return df_vendas


def extract_data_ranking(sql_ranking):
    df_produto = pd.read_sql(sql_ranking, engine)
    return df_produto


