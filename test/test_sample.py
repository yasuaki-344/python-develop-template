"""Unit test example."""
# Copyright (c) 2020 Yasuaki Miyoshi.
#
# This software is released under the MIT License.
# see http://opensource.org/licenses/mit-license.php

import unittest


class TestSample(unittest.TestCase):
    """Provide unit test."""

    def setUp(self):
        """Prepare the test fixture."""
        print("set up process")

    def tearDown(self):
        """Tidy up after the test method has been run."""
        print("tear down process")

    def test_execute(self):
        """Example."""
        print("execute process")
