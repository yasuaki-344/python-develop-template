"""Declaration of DI containers."""
# Copyright (c) 2020 Yasuaki Miyoshi.
#
# This software is released under the MIT License.
# see http://opensource.org/licenses/mit-license.php

import dependency_injector.containers as containers
import dependency_injector.providers as providers

from writer import Test


class ApplicationContainer(containers.DeclarativeContainer):
    """Inversion of control container of application.

    Args:
        containers ([type]): [description]
    """

    application = providers.Factory(
        Test,
        message="hello world"
    )
