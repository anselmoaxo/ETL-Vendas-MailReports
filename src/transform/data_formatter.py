


def transform_vendas(df_vendas):
    # Seleciona e renomeia colunas
    df_vendas = df_vendas[['nfe01_000_nota', 'nfe01_013_demi', 'nfe01_332_vprod',
                           'nfe01_000_cliente', 'nfe01_000_gerafaturamento']]
    df_vendas = df_vendas.rename(columns={
        'nfe01_000_nota': 'nota',
        'nfe01_013_demi': 'data_emissao',
        'nfe01_332_vprod': 'valor',
        'nfe01_000_cliente': 'cliente',
        'nfe01_000_gerafaturamento': 'gerafaturamento'
    })

    # Ordena os dados
    df_vendas = df_vendas.sort_values(by=['data_emissao', 'nota'], ascending=False).reset_index(drop=True)

    # Filtra clientes com ID maior que 0
    df_vendas = df_vendas[df_vendas['cliente'] > 0]

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
    df_vendas = df_vendas.sort_values(by='ultima_dt_compra', ascending=False)

    return df_vendas
