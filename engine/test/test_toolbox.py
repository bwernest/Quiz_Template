"""___Modules_______________________________________________________________"""

# Python
import os
import sys

# bwizz
from .asserts import Assert
from ..utils.toolbox import ToolBox

"""___Tests_________________________________________________________________"""


class TestToolBox(Assert):

    def test_normalize_string(self) -> None:
        toolbox = ToolBox("test")

        values = [
            "soirée",
            "Porco Rosso",
            "àeéèêîôùû-'"
        ]

        expecteds = [
            "soiree",
            "porcorosso",
            "aeeeeiouu"
        ]

        for value, expected in zip(values, expecteds):
            result = toolbox.normalize_string(value)
            self.assertEqual(expected, result, f"{expected} != {result}")
