"""Unit test example."""
# Copyright (c) 2020 Yasuaki Miyoshi.
#
# This software is released under the MIT License.
# see http://opensource.org/licenses/mit-license.php

import unittest


class TestSample(unittest.TestCase):
    """Provide unit test."""

    def setUp(self) -> None:
        """Prepare the test fixture."""
        print("set up process")

    def tearDown(self) -> None:
        """Tidy up after the test method has been run."""
        print("tear down process")

    def test_execute(self) -> None:
        """Example."""
        print("execute process")
