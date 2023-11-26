import logging
import os

import psycopg2


class PostgresConnectionError(RuntimeError):
    pass


class PostgresConnection:
    __connection = None
    __credentials = None

    def __init__(self):
        raise RuntimeError('Constructor should not be called')

    @staticmethod
    def open_connection():
        PostgresConnection.__init_connection()

    @staticmethod
    def execute_no_return(query, args=()):
        try:
            cursor = PostgresConnection.__connection.cursor()
            cursor.execute(query, args)
            PostgresConnection.__connection.commit()
        except Exception as error:
            logging.error('database exception: %s', error)
            PostgresConnection.__connection.rollback()
            raise error

    @staticmethod
    def execute(query, args=()):
        try:
            cursor = PostgresConnection.__connection.cursor()
            cursor.execute(query, args)
            PostgresConnection.__connection.commit()
            return cursor.fetchall()
        except Exception as error:
            logging.error('database exception: %s', error)
            PostgresConnection.__connection.rollback()
            raise error

    @staticmethod
    def __init_connection():
        env_vars = os.environ.keys()
        if (
            'PG_DB' not in env_vars
            or 'PG_USER' not in env_vars
            or 'PG_PASS' not in env_vars
            or 'PG_HOST' not in env_vars
            or 'PG_PORT' not in env_vars
        ):
            raise PostgresConnectionError('Not all vars are specified')

        connection_dict = dict(
            database=os.environ.get('PG_DB'),
            user=os.environ.get('PG_USER'),
            password=os.environ.get('PG_PASS'),
            host=os.environ.get('PG_HOST'),
            port=os.environ.get('PG_PORT'),
        )
        logging.error(connection_dict)

        PostgresConnection.__connection = psycopg2.connect(
            **connection_dict
        )
