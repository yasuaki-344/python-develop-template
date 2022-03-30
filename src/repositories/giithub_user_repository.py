from typing import Any, Dict

import requests


class GitHubUserRepository:

    def __init__(self):
        self.__rest_api_url = "https://api.github.com"

    def get_user_info(self, user: str) -> Dict[str, Any]:
        res = requests.get(f"{self.__rest_api_url}/users/{user}")
        return res.json()
