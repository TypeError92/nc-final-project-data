import dotenv
import os

from psycopg2.pool import SimpleConnectionPool
from root import root
from urllib import parse


env = os.getenv

if python_env := env('PYTHON_ENV') == 'prod':
    print('Production environment detected.')

else:
    if not python_env:
        print('No PYTHON_ENV detected, defaulting to "dev".')
        python_env = 'dev'

    print('No production environment detected, configuring local environment.')
    path = os.path.join(root, '.env.' + python_env)
    print('Loading .env from', path)
    dotenv.load_dotenv(path)

    port = env('PGPORT')
    if not port:
        port = 5432
    pg_database = env('PGDATABASE')

if database_url := env('DATABASE_URL'):
    parse.uses_netloc.append('postgres')
    url = parse.urlparse(database_url)
    pool = SimpleConnectionPool(1,
                                20,
                                user=url.username,
                                password=url.password,
                                host=url.hostname,
                                port=url.port)
elif pg_database := env('PGDATABASE'):
    pool = SimpleConnectionPool(1,
                                20,
                                dbname=pg_database,
                                port=env('PGPORT'))
else:
    raise Exception('No database specified.')
