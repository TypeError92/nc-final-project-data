import dotenv
import os
import psycopg2

from definitions import ROOT_DIR

def connect(env_name):
    if os.getenv('PYTHON_ENV') == 'SERVER':
        # Server environment
        print('Server environment detected.')
    else:
        # Local environment
        print('No server environment detected, configuring local environment.')
        path = ROOT_DIR + '/.env.' + env_name
        dotenv.load_dotenv(path)
        port=os.getenv('PGPORT') if os.getenv('PGPORT') else 5432
    database = os.getenv('DATABASE_URL') if os.getenv('DATABASE_URL') else os.getenv('PGDATABASE')
    if not database:
        raise Exception('No database specified.')
    else:
        print(f'Connecting @{env_name}')
        connection = psycopg2.connect(dbname=database,
                                      port=port)
    return connection
