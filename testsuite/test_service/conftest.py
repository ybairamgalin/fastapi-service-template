import logging

import pytest

import utils
from client import service_client
from client import postgres_client


def pytest_configure(config):
    pg_credentials = utils.get_pg_credentials()
    postgres_client.PostgresConnection.open_connection(pg_credentials)


@pytest.fixture(autouse=True)
def db_cleanup():
    pg_credentials = utils.get_pg_credentials()
    utils.run_pgmigrate(pg_credentials)
    yield
    utils.cleanup_database()


@pytest.fixture()
def service():
    return service_client.ServiceClient()
