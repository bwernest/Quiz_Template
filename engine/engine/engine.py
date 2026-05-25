"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ..utils import *
from ..parser.parser import Parser

"""___Classes___________________________________________________________________________________"""


class Engine(Parser):

    chapters = {}

    # API resources
    active_question: str = "Question par défaut"
    active_guess_entry: str = "Guess Entry par défaut"
    active_correction: str = "Correction par défaut"

    def start(self) -> None:
        self.chapters = self.get_data()

    def give_answer(self, answer: str) -> None:
        if answer == "":
            self.active_correction = "Bah alors tu connais pas la réponse gros con ?"
        else:
            self.active_correction = "Le système de correction n'est pas encore implémenté dommage."
