"""___Modules_______________________________________________________________"""

# bwizz
from .save import Save
from ..utils import *

# Python
from nicegui import ui
import numpy as np
from random import shuffle
from time import sleep
from typing import Dict, List, Literal, Tuple

"""___Classes_______________________________________________________________"""


class Engine(Save):

    def start(self) -> None:
        self.init_chapters()
        self.import_data()
        self.setup_fenetre("home", normal_mode_button=self.play_quiz, competitive_mode_button=self.play_quiz_competitive)
        self.start_fenetre()

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
        self.reset_question_index()

    def play_quiz(self, competitive: bool = False) -> None:
        competitive = False if competitive is not bool else competitive
        duree = self.competitive_mode_length if competitive else self.normal_mode_length
        bg_color = "red" if competitive else "blue"

        self.setup_fenetre("quiz", bg_color=bg_color)
        questions = self.get_questions(duree, competitive)
        self.init_quiz(questions)
        self.start_timer()
        self.questionner()

    def play_quiz_competitive(self) -> None:
        self.play_quiz(competitive=True)
        self.current_frame.configure(bg=self.color_BG_competitive)

    def questionner(self) -> None:
        self.set_question_result_label("")
        index = self.get_question_index
        if index < len(self.questions):
            self.question = self.questions[index]
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
        self.set_question_label(question_text)
        self.set_guess_entry()

        # Prevent spam
        self.set_validation_button(self.valider)
        self.guess_entry.on("keydown.enter", self.valider)

    def valider(self, event=None) -> None:

        # Prevent spam
        self.set_validation_button()
        self.guess_entry.on("keydown.enter", lambda: None)
        {
            "Q": self.corriger_Q,
            "I": self.corriger_I,
            "S": self.corriger_S,
            "L": self.corriger_L,
        }[self.question["type"]]()  # type: ignore
        
        self.guess_entry.set_value('')  # Vider le champ de saisie

    def corriger_Q(self) -> None:
        guess = self.guess_entry.value.strip().lower()
        self.guesses.append(guess)
        answer = self.questions[self.question_index]["reponse"]
        correct_answer = self.answer_is_correct(guess, answer)  # type: ignore
        self.deal_with_correction(correct_answer, answer)       # type: ignore

    def corriger_I(self) -> None:
        pass

    def corriger_S(self) -> None:
        guess = self.guess_entry.value.strip().lower()
        self.guesses.append(guess)
        for answer in self.answers:
            correct_answer = self.answer_is_correct(guess, answer)  # type: ignore
            if correct_answer:
                self.given_answers.append(answer)
                break
        self.deal_with_correction(correct_answer, answer)       # type: ignore

    def corriger_L(self) -> None:
        guess = self.guess_entry.value.strip().lower()
        self.guesses.append(guess)
        answer = self.question["reponse"][self.questions_list_index]
        correct_answer = self.answer_is_correct(guess, answer)  # type: ignore
        self.deal_with_correction(correct_answer, answer)       # type: ignore

    def deal_with_correction(self, correct_answer: bool, answer: str) -> None:

        # Bonne réponse
        if correct_answer:
            self.set_question_result_label("Correct ✔")
            shift = 500
            self.quiz_results.append(True)

        # Mauvaise réponse
        else:
            self.set_question_result_label(f"Non ✘\n{answer}")
            shift = 2000
            self.quiz_results.append(False)
        sleep(shift)
        self.questionner()

    def end_quiz(self) -> None:

        self.end_timer()
        # for r, result in enumerate(self.quiz_results):
        #     if result:
        #         element = self.questions[r]
        #         self.scores[element] += 1

        # self.erase_save()
        self.setup_fenetre("conclusion")
