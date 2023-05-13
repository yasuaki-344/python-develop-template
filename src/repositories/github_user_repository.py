"""Repository class example."""
from typing import Any

import requests


class GitHubUserRepository:
    """Repository example."""

    def __init__(self) -> None:
        """Initialize a new instance of GitHubUserRepository."""
        self.__rest_api_url = "https://api.github.com"

    def get_user_info(self, user: str) -> Any:
        """Get user information by using GitHub REST API.

        Args:
            user (str): _description_

        Returns:
            Dict[str, Any]: _description_
        """
        res = requests.get(f"{self.__rest_api_url}/users/{user}")
        return res.json()
