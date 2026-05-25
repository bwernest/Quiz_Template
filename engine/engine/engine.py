"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ..parser.parser import Parser

"""___Classes___________________________________________________________________________________"""


class Engine(Parser):

    chapters = {}

    def start(self) -> None:
        self.get_data()
