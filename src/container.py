"""Declaration of DI containers."""
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from use_cases.github_user_interactor import GitHubUserInteractor


class Container(containers.DeclarativeContainer):
    """Inversion of control container of application."""

    service = providers.Factory(GitHubUserInteractor)
