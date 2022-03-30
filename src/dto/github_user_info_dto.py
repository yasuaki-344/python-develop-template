import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class GitHubUserInfoDto:
    login: str
    url: str
    followers: int
    following: int
