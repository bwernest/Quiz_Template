"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ..utils import *
from ..parser.parser import Parser

# Python
from random import shuffle

"""___Classes___________________________________________________________________________________"""


class Engine(Parser):

    chapters = {}

    # API resources
    active_question_index: int = 0
    active_guess_entry: str = "Guess Entry par défaut"
    active_correction: str = "Correction par défaut"

    active_chapter: str = "Chapitre par défaut"
    steps: List[Dict[Literal["question", "reponse"], str]] = [{"question": "", "reponse": ""}]

    @property
    def active_question(self) -> str:
        return self.steps[self.active_question_index]["question"]

    @property
    def active_reponse(self) -> str:
        return self.steps[self.active_question_index]["reponse"]

    def start(self) -> None:
        self.chapters = self.get_data()
    
    def setup_game(self) -> None:
        self.steps = []
        self.active_question_index = 0
        self.active_chapter = self.quiz_theme
        self.active_correction = ""

        question_pool : List = self.chapters[self.active_chapter]["data"]   # type:ignore
        shuffle(question_pool)
        self.setup_questions(question_pool[:min(len(question_pool), self.quiz_length)])

    def setup_questions(self, question_pool: List[Dict]) -> None:
        self.steps = []
        capsules = self.get_capsules()
        for step in question_pool:
            question = capsules[step["type"]].replace(".", step["question"])
            self.steps.append({"question": question, "reponse": step["reponse"]})

    def go_next_question(self) -> None:
        self.active_question_index += 1
        self.active_correction = ""

    def get_capsules(self) -> Dict[Literal["Q", "I"], str]:
        capsules = {}
        for qtype in ["I", "Q"]:
            if f"capsule_{qtype}" in self.chapters[self.active_chapter]:
                capsules[qtype] = self.chapters[self.active_chapter][f"capsule_{qtype}"]
            else:
                capsules[qtype] = "."
        return capsules

    def give_answer(self, answer: str) -> None:
        if answer == "":
            self.active_correction = "Bah alors tu connais pas la réponse gros con ?"
        elif self.correct(answer, self.active_reponse):
            self.active_correction = "BIEN JOU2"
        else:
            self.active_correction = "C'est pas ça gros naze"

    def correct(self, guess: str, answer: str) -> bool:
        return guess.lower() == answer.lower()
