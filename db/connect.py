import dotenv
import os
import psycopg2

from definitions import ROOT_DIR

def connect(env_name):
    path = ROOT_DIR + '/.env.' + env_name
    print(path)
    dotenv.load_dotenv(path)
    user = os.getenv('PGUSER')
    database = os.getenv('PGDATABASE')
    print(database)
    connection = psycopg2.connect(host='localhost',
                                  port=5432,
                                  user=user,
                                  dbname=database)
    return connection
