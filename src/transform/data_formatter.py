import pandas as pd


def transform_vendas(df_vendas):
    # Seleciona e renomeia colunas
    df_vendas = df_vendas[['cli01_razao', 'nfe01_000_nota', 'nfe01_013_demi', 
                           'nfe01_341_vnf']]
    df_vendas = df_vendas.rename(columns={
        'cli01_razao': 'cliente',
        'nfe01_000_nota': 'nota',
        'nfe01_013_demi': 'data_emissao',
        'nfe01_341_vnf': 'valor'
    })

    # Ordena os dados
    df_vendas = df_vendas.sort_values(by=['data_emissao', 'nota'], ascending=False).reset_index(drop=True)



    # Agrupa por cliente e calcula estatísticas
    df_vendas = df_vendas.groupby(['cliente']).agg({
        'nota': 'count',
        'valor': 'sum',
        'data_emissao': 'max'
    }).rename(columns={
        'nota': 'qtd_notas',
        'valor': 'valor_total',
        'data_emissao': 'ultima_dt_compra'
    }).reset_index()

    # Ordena por data de última compra
    df_vendas = df_vendas.sort_values(by='valor_total', ascending=False)
    df_vendas.to_excel('data/output/vendas.xlsx', index=False)

    return df_vendas
