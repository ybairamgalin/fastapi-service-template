import os


class PostgresConnectionError(RuntimeError):
    pass


def get_pg_credentials():
    env_vars = os.environ.keys()
    if (
            'PG_DB' not in env_vars
            or 'PG_USER' not in env_vars
            or 'PG_PASS' not in env_vars
            or 'PG_HOST' not in env_vars
            or 'PG_PORT' not in env_vars
    ):
        raise PostgresConnectionError('Not all vars are specified')

    return dict(
        database=os.environ.get('PG_DB'),
        user=os.environ.get('PG_USER'),
        password=os.environ.get('PG_PASS'),
        host=os.environ.get('PG_HOST'),
        port=os.environ.get('PG_PORT'),
    )
