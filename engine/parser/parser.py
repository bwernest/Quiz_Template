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

    def get_data(self) -> Dict:

        return self.read_txt(self.paths["file_data"])
