import os
from psycopg2.pool import SimpleConnectionPool
from urllib import parse

env = os.getenv


if database_url := env('DATABASE_URL'):
    parse.uses_netloc.append('postgres')
    url = parse.urlparse(database_url)
    pool = SimpleConnectionPool(1,
                                20,
                                user=url.username,
                                password=url.password,
                                host=url.hostname,
                                port=url.port)
if pg_database := env('PGDATABASE'):
    pool = SimpleConnectionPool(1,
                                20,
                                dbname=pg_database,
                                port=env('PGPORT'))
else:
    raise Exception('No database specified.')
