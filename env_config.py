import dotenv
import os
from definitions import ROOT_DIR


class EnvironmentConfigurationError(Exception):
    pass


print(f'Cofiguring environment...')

env = os.getenv

if python_env := env('PYTHON_ENV') == 'prod':
    print('Production environment detected.')
else:
    if not python_env:
        print('No PYTHON_ENV detected, defaulting to "dev".')
        python_env = 'dev'

    print('No production environment detected, configuring local environment.')
    path = os.path.join(ROOT_DIR, '.env.' + python_env)
    print(path, os.path.isfile(path))
    dotenv.load_dotenv(path)
    port = env('PGPORT')
    if not port:
        port = 5432

# Ensure that database has been specified
if not (env('PGDATABASE') or env('DATABASE_URL')):
    raise EnvironmentConfigurationError('No database specified.')
