"""example usecase class implementation"""
from repositories.giithub_user_repository import GitHubUserRepository


class GitHubUserInteractor:
    """This is just example"""

    def __init__(self, repository: GitHubUserRepository):
        self.__repository = repository

    def get_user_information(self):
        res = self.__repository.get_user_info("defunkt")
        print(res)
