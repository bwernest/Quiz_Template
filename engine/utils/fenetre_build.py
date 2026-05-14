"""___Modules_______________________________________________________________"""

# bwizz
from . import *
from .quiz_toolbox import QuizToolBox

# Python
from nicegui import ui
import numpy as np
from typing import Callable, Dict, Literal, Optional, Tuple

"""___Classes_______________________________________________________________"""


class FenetreBuilder(QuizToolBox):

    font_size_buff: float = 1.0

    def font(self, text_type: Literal["title", "text", "small"], *args) -> Tuple:
        """
        text_type in [title, text, small]
        """
        text_types = {"title": self.font_size_title,
                      "text": self.font_size_text, "small": self.font_size_small}
        font = (self.font_type, int(text_types[text_type]*self.font_size_buff))
        for arg in args:
            font += (arg,)
        return font

    """___Home___"""

    def set_normal_mode_button(self, fct: Callable) -> None:
        ui.button("Partie Classique", on_click=fct)

    def set_competitive_mode_button(self) -> None:
        ui.button("Partie Compétitive", on_click=self.play_quiz_competitive)

    def set_chapter_button(self) -> None:
        ui.button("Sélection des chapitres", on_click=lambda: self.setup_fenetre("chapter", chapter=self.chapters))

    def set_parameter_button(self) -> None:
        ui.button("Paramètres", on_click=lambda: self.setup_fenetre("parameter"))

    """___Chapters___"""

    def set_home_button(self) -> None:
        ui.button("Menu", on_click=lambda: self.setup_fenetre("home"))

    """___Parameter___"""

    def set_increase_font_size_button(self) -> None:
        ui.button("Augmenter la taille de police", on_click=self.increase_font_size)

    def set_decrease_font_size_button(self) -> None:
        ui.button("Diminuer la taille de police", on_click=self.decrease_font_size)

    def increase_font_size(self) -> None:
        self.font_size_buff += 0.1
        self.setup_fenetre("parameter")

    def decrease_font_size(self) -> None:
        self.font_size_buff = max(0.4, self.font_size_buff-0.1)
        self.setup_fenetre("parameter")

    """___Quiz___"""

    def set_question_label(self, message: str) -> None:
        ui.label(message)

    def set_guess_entry(self) -> None:
        self.guess_entry = ui.input("")

    def set_validation_button(self, action: Callable = lambda: 1+1) -> None:
        ui.button("Valider", on_click=action)

    def set_question_result_label(self, message: str) -> None:
        ui.label(message)

    """___Results___"""

    def set_conclusion_label(self) -> None:
        text = "Résultats"
        text += "\n\nBonnes Réponses ✔ :\n"
        for r, result in enumerate(self.quiz_results):
            if result:
                text += f"{self.questions[r]["question"]} : {self.guesses[r]}\n"

        text += "\n"
        text += "Mauvaises Réponses ✘ :\n"
        for r, result in enumerate(self.quiz_results):
            if not result:
                text += f"{self.questions[r]["question"]} : {self.questions[r]["reponse"]}\n"

        ui.label(text)

    def set_score_label(self) -> None:
        score = int(np.sum(self.quiz_results))
        if score == len(self.quiz_results):
            displayed_score = "Score Parfait !"
        elif score == 0:
            displayed_score = "Score horrible !"
        else:
            displayed_score = f"Score : {score}/{len(self.quiz_results)}"
        ui.label(displayed_score)

    def set_timer_label(self) -> None:
        text = f"Temps : {round(self.quiz_time, 2)}s"
        ui.label(text)

    def set_replay_button(self) -> None:
        ui.button("Rejouer", on_click=self.play_quiz)

    def set_quit_button(self) -> None:
        ui.button("Quitter", on_click=self.kill_fenetre)
