"""example usecase class implementation"""
from business_logics.github_user_info_extractor import GitHubUserInfoExtractor
from repositories.giithub_user_repository import GitHubUserRepository


class GitHubUserInteractor:
    """This is just example"""

    def __init__(self, repository: GitHubUserRepository, business_logic: GitHubUserInfoExtractor):
        self.__repository = repository
        self.__business_logic = business_logic

    def get_user_information(self) -> None:
        res = self.__repository.get_user_info("defunkt")
        info = self.__business_logic.extract_user_info(res)
        print(info)
