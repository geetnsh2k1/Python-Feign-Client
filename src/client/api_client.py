import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        return self._request('GET', endpoint, params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None, files=None):
        return self._request('POST', endpoint, data=data, json=json, headers=headers, files=files)

    def put(self, endpoint, data=None, json=None, headers=None):
        return self._request('PUT', endpoint, data=data, json=json, headers=headers)

    def delete(self, endpoint, params=None, headers=None):
        return self._request('DELETE', endpoint, params=params, headers=headers)

    def _request(self, method, endpoint, params=None, data=None, json=None, headers=None, files=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(
            method,
            url,
            params=params,
            data=data,
            json=json,
            headers=headers,
            files=files
        )
        return self._parse_response(response)

    def _parse_response(self, response):
        raise NotImplementedError("Subclasses must implement _parse_response method")
