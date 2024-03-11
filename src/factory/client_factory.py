from src.client.add_post_client import AddPostAPIClient
from src.client.get_posts_client import GetPostsAPIClient


class ClientFactory:

    @staticmethod
    def get_posts(base_url: str) -> GetPostsAPIClient:
        return GetPostsAPIClient(base_url=base_url)

    @staticmethod
    def add_post(base_url: str) -> AddPostAPIClient:
        return AddPostAPIClient(base_url=base_url)
