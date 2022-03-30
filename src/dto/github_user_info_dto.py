import dataclasses


@dataclasses.dataclass
class GitHubUserInfoDto:
    login: str
    url: str
    followers: int
    following: int
