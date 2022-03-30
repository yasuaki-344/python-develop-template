from typing import Any, Dict

from dto.github_user_info_dto import GitHubUserInfoDto


class GitHubUserInfoExtractor:
    def __init__(self) -> None:
        pass

    def extract_user_info(self, json: Dict[str, Any]) -> GitHubUserInfoDto:
        dto = GitHubUserInfoDto.from_dict(json)
        return dto
