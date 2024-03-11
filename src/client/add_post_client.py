from src.client.api_client import APIClient
from src.dataclass.posts import Post


class AddPostAPIClient(APIClient):
    _instance = None

    def __new__(cls, base_url):
        if cls._instance is None:
            cls._instance = super(AddPostAPIClient, cls).__new__(cls)
        return cls._instance

    def _parse_response(self, response) -> Post:
        data = response.json()
        return Post(**data)
