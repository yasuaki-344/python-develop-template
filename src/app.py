"""Application entry point"""

from dependency_injector.wiring import Provide, inject

from container import Container
from use_cases.github_user_interactor import GitHubUserInteractor


@inject
def main(service: GitHubUserInteractor = Provide[Container.service]):
    """Sets up dependency injection and run application."""
    service.get_user_information()


if __name__ == "__main__":
    """Entry point of application"""
    container = Container()
    container.wire(modules=[__name__])

    main()
