import pandas as pd
from src.extract.db_extractor import caminho_sql_ranking, extract_data_ranking


ranking = caminho_sql_ranking()
df_ranking = extract_data_ranking(ranking)

df_ranking = df_ranking.rename(columns={
    'nfe04_103_xprod': 'Produto',
    'B.nfe04_101_cprod': 'CodigoProd.'
})
df_ranking = df_ranking.head(10)
df_ranking.to_excel('data/output/ranking_produto.xlsx', index=False)