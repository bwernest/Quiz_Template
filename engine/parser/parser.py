"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ..utils import *
from ..utils.toolbox import ToolBox

# Python
import os
import pickle
import json

"""___Classes___________________________________________________________________________________"""


class Parser(ToolBox):

    def get_data(self) -> None:

        raw_data = self.read_txt(self.paths["file_data"])
        print(raw_data)
