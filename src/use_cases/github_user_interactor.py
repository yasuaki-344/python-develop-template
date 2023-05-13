"""example use case class implementation."""
from business_logics.github_user_info_extractor import GitHubUserInfoExtractor
from repositories.github_user_repository import GitHubUserRepository


class GitHubUserInteractor:
    """This is just example."""

    def __init__(self, repository: GitHubUserRepository, business_logic: GitHubUserInfoExtractor):
        """Initialize a new instance of GitHubUserInteractor.

        Args:
            repository (GitHubUserRepository): _description_
            business_logic (GitHubUserInfoExtractor): _description_
        """
        self.__repository = repository
        self.__business_logic = business_logic

    def get_user_information(self) -> None:
        """Get user information."""
        res = self.__repository.get_user_info("defunkt")
        info = self.__business_logic.extract_user_info(res)
        print(info)
