"""___Modules_______________________________________________________________"""

# bwizz
from ..utils import *
from ..utils.fenetre_setup import FenetreSetup

# Python
import tkinter as tk
from tkinter import ttk
from typing import Tuple

"""___Classes_______________________________________________________________"""


class Fenetre(FenetreSetup):

    exists: bool = False

    def setup_fenetre(self, config: str, **kwargs) -> None:
        configs = {
            "home": self.setup_fenetre_home,
            "quiz": self.setup_fenetre_quiz,
            "conclusion": self.setup_fenetre_conclusion,
            "chapter": self.setup_fenetre_chapter,
            "parameter": self.setup_fenetre_parameter,
        }

        if not self.exists:
            self.main_fenetre = tk.Tk()
            self.main_fenetre.geometry(
                f"{self.window_size[0]}x{self.window_size[1]}")
            self.main_fenetre.title(self.window_title)
            self.main_fenetre.bind("<Escape>", self.kill_fenetre)

            for chapter in self.chapters.keys():
                self.chapters[chapter] = tk.BooleanVar(value=True)

            self.style = ttk.Style()
            self.style.theme_use("clam")

            self.exists = True

        self.clear_frame()
        self.main_fenetre.unbind("m")
        self.main_fenetre.unbind("r")
        self.current_frame = tk.Frame(self.main_fenetre)
        self.current_frame.configure(bg=self.color_BG_menu)
        self.current_frame.pack(fill="both", expand=True)
        configs[config](normal_mode_button=self.play_quiz, **kwargs)

    def init_quiz(self, questions: list, answers: list) -> None:
        self.questions = questions
        self.answers = answers
        self.guesses = []
        self.quiz_results = []
        self.reset_question_index()

    def reset_question_index(self) -> None:
        self.question_index = -1

    @property
    def get_question_index(self) -> int:
        self.question_index += 1
        return self.question_index

    def start_fenetre(self) -> None:
        self.main_fenetre.mainloop()

    def kill_fenetre(self, envent=None) -> None:
        self.main_fenetre.destroy()
