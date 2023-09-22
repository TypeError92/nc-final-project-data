import dotenv
import os
from psycopg2.pool import SimpleConnectionPool
from urllib import parse
from definitions import ROOT_DIR


def pool(env_name):
    if os.getenv('PYTHON_ENV') == 'SERVER':
        # Server environment
        print('Server environment detected.')
    else:
        # Local environment
        print('No server environment detected, configuring local environment.')
        path = ROOT_DIR + '/.env.' + env_name
        dotenv.load_dotenv(path)
        port=os.getenv('PGPORT') if os.getenv('PGPORT') else 5432
    if database_url := os.getenv('DATABASE_URL'):
        parse.uses_netloc.append('postgres')
        url = parse.urlparse(database_url)
        pool = SimpleConnectionPool(1, 20,
                                                   user=url.username,
                                                   password=url.password,
                                                   host=url.hostname,
                                                   port=url.port)
    elif pg_database := os.getenv('PGDATABASE'):
        pool = SimpleConnectionPool(1, 20, dbname=pg_database, port=port)
    else:
        raise Exception('No database specified.')
    return pool
