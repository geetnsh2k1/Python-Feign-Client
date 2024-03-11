from src.external_api_handler import ExternalAPIHandlers

if __name__ == '__main__':
    print(
        ExternalAPIHandlers.add_post(
            title="Lord",
            body="Mehul",
            user_id=1
        )
    )
