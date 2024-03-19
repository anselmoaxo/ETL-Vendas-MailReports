import sqlalchemy as sa
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("DATABASE_URL")


engine = sa.create_engine(database_url)