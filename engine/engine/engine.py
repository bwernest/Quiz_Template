"""___Modules_______________________________________________________________"""

# bwizz
from ..utils import *
from .fenetre import Fenetre

# Python
import numpy as np
from tkinter import BooleanVar
from typing import Dict, List, Tuple

"""___Classes_______________________________________________________________"""


class Engine(Fenetre):

    def start(self) -> None:
        self.init_chapters()
        self.import_data()
        self.import_save()
        self.setup_fenetre("home")
        self.start_fenetre()

    def import_data(self) -> None:
        self.data = self.import_data_file()
        self.elements: Dict[str, str] = {}
        for chapter in self.data.keys():
            self.chapters[chapter] = True
            for key, value in self.data[chapter].items():
                self.elements[key] = value

    def import_save(self) -> None:
        self.save = self.import_save_file()
        self.scores = {}
        self.attempts = {}

        # No save
        if self.save == []:
            pass

        # Save exists
        else:
            for element, score, attempt in self.save:
                self.scores[element] = score
                self.attempts[element] = attempt

        self.fix_save()

    def reset_save(self) -> None:
        save_elements = [element for element, _, _ in self.save]
        for element in save_elements:
            self.scores[element] = 0
            self.attempts[element] = 0
        self.erase_save()

    def fix_save(self) -> None:
        save_elements = [element for element, _, _ in self.save]
        for element in self.elements:
            if element not in save_elements:
                self.scores[element] = 0
                self.attempts[element] = 0

    def erase_save(self) -> None:
        save = ""
        for element in self.elements:
            save += f"{element}:{self.scores[element]}:{self.attempts[element]}\n"
        self.write_txt(self.paths["file_save"], save[:-1], extension="")

    def get_questions(self, duree: int, competitive: bool) -> Tuple[List[str], List[str]]:
        """
        Retourne 2 listes questions et answers.
        Des listes de strings comme on en fait plus.
        """
        played_elements = {}
        for chapter, check in self.chapters.items():
            if check.get():
                for key, value in self.data[chapter].items():
                    played_elements[key] = value
        if len(played_elements) <= duree:
            return list(played_elements.keys()), list(played_elements.values())

        # Liste pondérée des indices
        ponderated_elements = []
        if competitive:
            ponderated_elements = list(self.elements.keys())
        else:
            for element in played_elements.keys():
                score = self.scores[element]
                attempt = self.attempts[element]
                ponderated_elements.extend([element]*min(20, int(attempt-score+1)**2))
                if score == 0:
                    ponderated_elements.extend([element]*10)
        lenP = len(ponderated_elements)

        # Tirage des questions
        questions = []
        for _ in range(duree):
            index = np.random.randint(0, lenP)
            while ponderated_elements[index] in questions:
                lenP -= 1
                ponderated_elements.pop(index)
                index = np.random.randint(0, lenP)
            lenP -= 1
            questions.append(ponderated_elements.pop(index))
            self.attempts[questions[-1]] += 1

        # Réponses
        answers = []
        for element in questions:
            answers.append(self.elements[element])

        return questions, answers

    def play_quiz(self, competitive: bool = False) -> None:
        competitive = False if competitive is not bool else competitive
        duree = self.competitive_mode_length if competitive else self.normal_mode_length
        bg_color = "red" if competitive else "blue"

        self.setup_fenetre("quiz", bg_color=bg_color)
        questions, answers = self.get_questions(duree, competitive)
        self.init_quiz(questions, answers)
        self.start_timer()
        self.questionner()

    def play_quiz_competitive(self) -> None:
        self.play_quiz(competitive=True)
        self.current_frame.configure(bg=self.color_BG_competitive)

    def questionner(self) -> None:
        self.reset_question_result_label("")
        index = self.get_question_index
        if index < len(self.questions):
            self.reset_question_label(
                f"Que signifie {self.questions[index]} ?")
            self.reset_guess_entry()

            # Prevent spam
            self.reset_validation_button(self.valider)
            self.main_fenetre.bind("<Return>", self.valider)
        else:
            self.end_quiz()

    def valider(self, event=None) -> None:

        # Prevent spam
        self.reset_validation_button()
        self.main_fenetre.unbind("<Return>")

        guess = self.guess_entry.get()
        self.guesses.append(guess)
        answer = self.answers[self.question_index]
        correct_answer = self.answer_is_correct(guess, answer)

        # Bonne réponse
        if correct_answer:
            self.reset_question_result_label("Correct ✔")
            shift = 500
            self.quiz_results.append(True)

        # Mauvaise réponse
        else:
            self.reset_question_result_label(f"Non ✘\n{answer}")
            shift = 2000
            self.quiz_results.append(False)
        self.current_frame.after(shift, self.questionner)

    def end_quiz(self) -> None:

        self.end_timer()
        for r, result in enumerate(self.quiz_results):
            if result:
                element = self.questions[r]
                self.scores[element] += 1

        self.erase_save()
        self.setup_fenetre("conclusion")
