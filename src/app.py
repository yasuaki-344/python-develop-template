"""Application entry point"""

from container import Service, Container
from dependency_injector.wiring import Provide, inject


@inject
def main(service: Service = Provide[Container.service]):
    """Sets up dependency injection and run application.
    """
    service.sample()


if __name__ == "__main__":
    """Entry point of application
    """
    container = Container()
    container.wire(modules=[__name__])

    main()
