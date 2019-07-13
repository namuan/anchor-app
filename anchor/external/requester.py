import json
import logging
import os
import requests
import requests_cache


class Requester:
    def __init__(self, timeout_secs=5, raise_for_status=True):
        self._raise_for_status = raise_for_status
        self.timeout_secs = timeout_secs
        self.is_offline = os.getenv("OFFLINE", "false").lower() == "true"
        if self.is_offline:
            logging.info("Offline mode: Setting up offline store")
            requests_cache.configure(
                '../offline_data/data_cache',
                backend='sqlite',
                expire_after=10000,
                allowable_methods=('GET', 'POST')
            )

    def raise_for_status(self, response):
        if self._raise_for_status:
            response.raise_for_status()

    def request_post(self, resource, user, password, post_data):
        try:
            response = requests.post(
                url=resource,
                timeout=self.timeout_secs,
                headers={
                    "Content-Type": "application/json"
                },
                auth=(
                    user,
                    password
                ),
                data=json.dumps(post_data)
            )
            logging.info('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            self.raise_for_status(response)
            if response.content:
                return response.json()
            else:
                return response.content
        except requests.exceptions.HTTPError as e:
            logging.info(f"Error Response {e}")
            raise ConnectionError(e)
        except requests.exceptions.RequestException as e:
            logging.info('HTTP Request failed')
            raise ConnectionError(e)

    def do_get(self, resource, kwargs):
        try:
            response = requests.get(
                url=resource,
                timeout=self.timeout_secs,
                **kwargs
            )
            self.raise_for_status(response)
            response_json = response.json()
            return response_json
        except requests.exceptions.HTTPError as e:
            logging.info(f"Error Response {e}")
            raise ConnectionError(e)
        except requests.exceptions.RequestException as e:
            logging.info('HTTP Request failed')
            logging.info(e)

    def do_post(self, resource, kwargs):
        try:
            response = requests.post(
                url=resource,
                timeout=self.timeout_secs,
                **kwargs
            )
            self.raise_for_status(response)
            response_json = response.json()
            return response_json
        except requests.exceptions.HTTPError as e:
            logging.info(f"Error Response {e}")
            raise ConnectionError(e)
        except requests.exceptions.RequestException as e:
            logging.info('HTTP Request failed')
            logging.info(e)

    def request_get(self, resource, user, password, params=None):
        if params is None:
            params = {}

        try:
            response = requests.get(
                url=resource,
                timeout=self.timeout_secs,
                params=params,
                auth=(
                    user,
                    password
                )
            )
            logging.info('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            self.raise_for_status(response)
            return response.json()
        except requests.exceptions.HTTPError as e:
            logging.info(f"Error Response {e}")
            raise ConnectionError(e)
        except requests.exceptions.RequestException as e:
            logging.info('HTTP Request failed')
            raise ConnectionError(e)
