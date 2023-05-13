"""Business logic example."""
from typing import Any, Dict

from dto.github_user_info_dto import GitHubUserInfoDto


class GitHubUserInfoExtractor:
    """Business logic class."""

    def __init__(self) -> None:
        """Initialize a new instance of GitHubUserInfoExtractor class."""
        pass

    def extract_user_info(self, json: Dict[str, Any]) -> Any:
        """Convert json data to GitHubUserInfoDto.

        Args:
            json (Dict[str, Any]): _description_

        Returns:
            GitHubUserInfoDto: _description_
        """
        dto = GitHubUserInfoDto.from_dict(json)  # type: ignore
        return dto
