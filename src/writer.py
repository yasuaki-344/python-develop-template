"""Sample class."""
# Copyright (c) 2020 Yasuaki Miyoshi.
#
# This software is released under the MIT License.
# see http://opensource.org/licenses/mit-license.php


class Test:
    """This is just example."""

    def __init__(self, message: str):
        """Initialize a new instance of Test class.

        Args:
            message (str): Example of argument.
        """
        self.__output_string = message

    def output(self):
        """Output string to console."""
        print(self.__output_string)
