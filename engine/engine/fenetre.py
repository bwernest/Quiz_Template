"""___Modules_______________________________________________________________"""

# bwizz
from ..utils import *
from ..utils.fenetre_setup import FenetreSetup

# Python
from nicegui import ui
from typing import Dict, List, Literal, Tuple

"""___Classes_______________________________________________________________"""


class Fenetre(FenetreSetup):

    exists: bool = False
    question: Dict[Literal["type", "question", "reponse"], str]
    questions: List[Dict[Literal["type", "question", "reponse"], str]]

    def setup_fenetre(self, config: str, **kwargs) -> None:
        {
            "home": self.setup_fenetre_home,
            "quiz": self.setup_fenetre_quiz,
            "parameter": self.setup_fenetre_parameter,
            "conclusion": self.setup_fenetre_conclusion,
        }[config](**kwargs)

    def reset_question_index(self) -> None:
        self.question_index = -1

    @property
    def get_question_index(self) -> int:
        self.question_index += 1
        return self.question_index

    def start_fenetre(self) -> None:
        ui.run()
