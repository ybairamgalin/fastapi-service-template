import os

from client import postgres_client


def cleanup_database():
    if 'PG_SCHEMA' not in os.environ.keys():
        raise RuntimeError('Schema is not specified')

    postgres_client.PostgresConnection.execute_no_return(
        f"""
            drop schema {os.environ.get('PG_SCHEMA')} cascade
        """
    )
    postgres_client.PostgresConnection.execute_no_return(
        """
            drop table public.schema_version
        """
    )
    postgres_client.PostgresConnection.execute_no_return(
        """
            drop type public.schema_version_type
        """
    )
