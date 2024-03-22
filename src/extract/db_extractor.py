from sqlalchemy import create_engine
import pandas as pd
from ..utils.database import database_url

engine = create_engine(database_url)
    
    
def extract_data(sql_query):
    df_vendas = pd.read_sql(sql_query, engine)
    return df_vendas