"""Declaration of DI containers."""
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from writer import Test

class Service:
    def __init__(self) -> None:
        self.__target = "hello world"

    def sample(self):
        print(self.__target)


class Container(containers.DeclarativeContainer):
    """Inversion of control container of application."""

    application = providers.Factory(
        Test,
        message="hello world"
    )

    service = providers.Factory(Service)
