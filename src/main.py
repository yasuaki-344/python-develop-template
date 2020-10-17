"""Entry point of application."""
# Copyright (c) 2020 Yasuaki Miyoshi.
#
# This software is released under the MIT License.
# see http://opensource.org/licenses/mit-license.php

from containers import ApplicationContainer

if __name__ == "__main__":
    app = ApplicationContainer.application()
    app.output()
