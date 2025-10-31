"""___Modules_______________________________________________________________"""

# Python
import os
import sys

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Project
from .asserts import Assert
from ..engine.engine import Engine

"""___Tests_________________________________________________________________"""


class TestEngine(Assert):

    def test_import(self) -> None:
        engine = Engine("test")
        engine.start()
        engine.import_data()
        result = engine.data
        self.assertIsInstance(result, dict)
        test_key = list(result.keys())[0]
        self.assertIsInstance(test_key, str)
        self.assertIsInstance(result[test_key], str)
