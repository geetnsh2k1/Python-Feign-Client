from src.client.api_client import APIClient
from src.dataclass.posts import Posts, Post


class GetPostsAPIClient(APIClient):
    _instance = None

    def __new__(cls, base_url):
        if cls._instance is None:
            cls._instance = super(GetPostsAPIClient, cls).__new__(cls)
        return cls._instance

    def _parse_response(self, response) -> Posts:
        data = response.json()
        posts: list[Post] = [Post(**d) for d in data]
        return Posts(posts=posts)
