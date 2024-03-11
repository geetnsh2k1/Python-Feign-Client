class APIConfig:
    def __init__(
            self,
            headers=None,
            body=None,
            files=None,
            query_params=None,
            headers_required_variables=None,
            body_required_variables=None,
            files_required_variables=None,
            query_params_required_variables=None,
    ):
        self.HEADERS = headers or {}
        self.BODY = body or {}
        self.FILE = files or {}
        self.QUERY_PARAMS = query_params or {}
        self.headers_required_variables = headers_required_variables or set()
        self.body_required_variables = body_required_variables or set()
        self.files_required_variables = files_required_variables or set()
        self.query_params_required_variables = query_params_required_variables or set()

    @staticmethod
    def replace_variables_in_dict(
            input_dict: dict,
            required_variables: set,
            variables: dict
    ):
        missing_variables = required_variables - set(variables.keys())
        if missing_variables:
            raise ValueError(f"Missing required variables: {', '.join(missing_variables)}")

        output_dict = {}
        for key, value in input_dict.items():
            if isinstance(value, dict):
                output_dict[key] = APIConfig.replace_variables_in_dict(
                    input_dict=value,
                    required_variables=required_variables,
                    variables=variables
                )
            elif isinstance(value, str):
                output_dict[key] = value.format(**variables)
            else:
                output_dict[key] = value
        return output_dict


ADD_POST_API_CONFIG = APIConfig(
    headers={
        "Content-Type": "application/json; charset=UTF-8"
    },
    body={
        "title": "{title}",
        "body": "{body}",
        "userId": "{userId}",
    },
    headers_required_variables={"X_API_KEY", "token"},
    body_required_variables={}
)
