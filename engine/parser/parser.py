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

    def get_data(self) -> Dict[str, Dict[str, str | List[str]]]:

        return self.read_json(self.paths["file_data"])
