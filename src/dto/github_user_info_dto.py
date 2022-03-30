"""Data transfer object example."""
import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class GitHubUserInfoDto:
    """This is example DTO."""

    login: str
    url: str
    followers: int
    following: int
