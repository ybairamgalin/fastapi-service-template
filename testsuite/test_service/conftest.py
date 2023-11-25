import pytest

import requests

from client import service_client


@pytest.fixture()
def service():
    return service_client.ServiceClient()
