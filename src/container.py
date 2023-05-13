"""Declaration of DI containers."""
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from business_logics.github_user_info_extractor import GitHubUserInfoExtractor
from repositories.github_user_repository import GitHubUserRepository
from use_cases.github_user_interactor import GitHubUserInteractor


class Container(containers.DeclarativeContainer):
    """Inversion of control container of application."""

    repository = providers.Singleton(GitHubUserRepository)  # types: ignore

    business_logic = providers.Factory(GitHubUserInfoExtractor)

    service = providers.Factory(
        GitHubUserInteractor, repository=repository, business_logic=business_logic
    )
