"""___Modules_______________________________________________________________"""

# Python
import os
import sys

# bwizz
from .asserts import Assert
from ..engine.engine import Engine

"""___Tests_________________________________________________________________"""


class TestEngine(Assert):

    def test_import(self) -> None:
        engine = Engine("test")
        engine.import_data()
        result = engine.data
        self.assertIsInstance(result, dict)
        test_key = list(result.keys())[0]
        self.assertIsInstance(test_key, str)
        self.assertIsInstance(result[test_key], str)
