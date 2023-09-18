import psycopg2
import os

db_name = os.getenv('PGDATABASE')
db_user = os.getenv('PGUSER')

db = psycopg2.connect(f'dbname={db_name} user={db_user}')