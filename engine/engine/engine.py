"""___Modules___________________________________________________________________________________"""

# bwizz
from .save import Save
from ..utils import *

# Python
import numpy as np
from random import shuffle
from time import sleep
from typing import Dict, List, Literal, Optional, Tuple

"""___Classes___________________________________________________________________________________"""


class Engine(Save):

    question_index: int
    active_question: str
    result_label: str

    @property
    def result_labels(self) -> Dict[bool, str]:
        return {
            True: "Correct ✔",
            False: "Non ✘"
        }

    def start(self) -> None:
        self.init_chapters()
        self.import_data()

    def import_data(self) -> None:
        self.data = self.import_data_file()
        self.elements: Dict[str, str] = {}
        for chapter in self.data.keys():
            self.chapters[chapter] = True   # type: ignore

    def get_questions(self, duree: int, competitive: bool) -> List[Dict[Literal["type", "question", "reponse"], str]]:
        """
        Retourne une liste de questions.
        """
        # Récupération des questions parmi les chapitres actifs
        questions = []
        for chapter, check in self.chapters.items():
            if check:
                for question in self.data[chapter]["questions"]:
                    questions.append(question)
        shuffle(questions)
        return questions[:min(duree, len(questions))]

    def init_quiz(self, questions: List[Dict[Literal["type", "question", "reponse"], str]]) -> None:
        self.questions = questions
        self.guesses = []
        self.quiz_results = []

    def setup_quiz(self, competitive: bool = False) -> None:
        competitive = False if competitive is not bool else competitive
        duree = self.competitive_mode_length if competitive else self.normal_mode_length
        self.question_index = 0

        questions = self.get_questions(duree, competitive)
        self.init_quiz(questions)
        self.start_timer()

    def play_quiz_competitive(self) -> None:
        self.setup_quiz(competitive=True)

    def questionner(self) -> None:
        if self.question_index < len(self.questions):
            self.question = self.questions[self.question_index]
            self.active_question = self.question["question"]
            {
                "Q": self.questionner_Q,
                "I": self.questionner_I,
                "S": self.questionner_S,
                "L": self.questionner_L,
            }[self.question["type"]]()
        else:
            self.end_quiz()

    def questionner_Q(self) -> None:
        self.give_question(self.question["question"])
    
    def questionner_L(self) -> None:
        self.questions_list_index = 0
        for question in self.question["question"]:
            self.give_question(question)
            self.questions_list_index += 1

    def questionner_S(self) -> None:
        self.given_answers = []
        self.answers = self.question["reponse"]
        for question in self.question["question"]:
            self.give_question(question)

    def questionner_I(self) -> None:
        self.give_question(self.question["question"])
        
    def give_question(self, question_text) -> None:
        self.active_question = question_text

    def valider(self, guess: Optional[str]) -> None:
        {
            "Q": self.corriger_Q,
            "I": self.corriger_I,
            "S": self.corriger_S,
            "L": self.corriger_L,
        }[self.question["type"]](guess)
        
    def corriger_Q(self, guess: Optional[str]) -> None:
        self.guesses.append(guess)
        answer = self.questions[self.question_index]["reponse"]
        correct_answer = self.answer_is_correct(guess, answer)
        self.deal_with_correction(correct_answer)

    def corriger_I(self, guess: Optional[str]) -> None:
        pass

    def corriger_S(self, guess: Optional[str]) -> None:
        self.guesses.append(guess)
        for answer in self.answers:
            correct_answer = self.answer_is_correct(guess, answer)
            if correct_answer:
                self.given_answers.append(answer)
                break
        self.deal_with_correction(correct_answer)

    def corriger_L(self, guess: Optional[str]) -> None:
        self.guesses.append(guess)
        answer = self.question["reponse"][self.questions_list_index]
        correct_answer = self.answer_is_correct(guess, answer)
        self.deal_with_correction(correct_answer)

    def deal_with_correction(self, answer_is_correct: bool) -> None:

        # Bonne réponse
        if answer_is_correct:
            self.result_label = self.result_labels[True]
            self.quiz_results.append(True)

        # Mauvaise réponse
        else:
            self.result_label = self.result_labels[False]
            self.quiz_results.append(False)
        self.question_index += 1

    def end_quiz(self) -> None:

        self.end_timer()
        # for r, result in enumerate(self.quiz_results):
        #     if result:
        #         element = self.questions[r]
        #         self.scores[element] += 1

        # self.erase_save()
