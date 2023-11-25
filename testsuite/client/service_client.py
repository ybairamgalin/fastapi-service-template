import os

import requests
import json

SERVICE_URL = 'SERVICE_URL'
SERVICE_PORT = 'SERVICE_PORT'


class ServiceClient:
    def __init__(self):
        env_vars = os.environ.keys()
        assert SERVICE_URL in env_vars
        assert SERVICE_PORT in env_vars
        self.service_url = (
            f'{os.environ.get(SERVICE_URL)}:{os.environ.get(SERVICE_PORT)}'
        )

    def get(self, path, headers=None, body_dict=None):
        response = requests.get(
            url=self.service_url+path,
            headers=headers if headers else None,
            data=json.dumps(body_dict) if body_dict else None,
        )
        return response

    def post(self, path, headers=None, body_dict=None):
        response = requests.post(
            url=self.service_url + path,
            headers=headers if headers else None,
            data=json.dumps(body_dict) if body_dict else None,
        )
        return response
