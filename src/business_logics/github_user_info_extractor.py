from dto.github_user_info_dto import GitHubUserInfoDto


class GitHubUserInfoExtractor:
    def __init__(self) -> None:
        pass

    def extract_user_info(self, json) -> GitHubUserInfoDto:
        dto = GitHubUserInfoDto(
            login=json["login"],
            url=json["url"],
            followers=json["followers"],
            following=json["following"],
        )
        return dto
