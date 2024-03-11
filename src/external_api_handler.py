import json

from src.config.api_config import APIConfig, ADD_POST_API_CONFIG
from src.constants.endpoints import ClientEndpoints
from src.dataclass.posts import Post, Posts
from src.factory.client_factory import ClientFactory


class ExternalAPIHandlers:
    @staticmethod
    def get_posts() -> Posts:
        try:
            get_posts_api_client = ClientFactory.get_posts(ClientEndpoints.Mockend.BASE)

            posts: Posts = (
                get_posts_api_client.get(
                    ClientEndpoints.Mockend.POSTS,
                )
            )

            return posts
        except Exception as e:
            print("[value-error]", e)
            raise e

    @staticmethod
    def add_post(
            title: str,
            body: str,
            user_id: int
    ) -> Post:
        try:
            add_post_api_client = ClientFactory.add_post(ClientEndpoints.Mockend.BASE)

            body_required_variables = {
                "title": title,
                "body": body,
                "userId": user_id
            }

            body = APIConfig.replace_variables_in_dict(
                input_dict=ADD_POST_API_CONFIG.BODY,
                required_variables=ADD_POST_API_CONFIG.body_required_variables,
                variables=body_required_variables
            )

            post: Post = (
                add_post_api_client.post(
                    ClientEndpoints.Mockend.POSTS,
                    data=json.dumps(body)
                )
            )

            return post
        except Exception as e:
            print("[value-error]", e)
            raise e
