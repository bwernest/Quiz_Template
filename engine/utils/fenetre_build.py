"""___Modules_______________________________________________________________"""

# bwizz
from . import *
from .quiz_toolbox import QuizToolBox

# Python
import numpy as np
import tkinter as tk
from typing import Callable, Dict, Literal, Optional, Tuple

"""___Classes_______________________________________________________________"""


class FenetreBuilder(QuizToolBox):

    current_frame: Optional[tk.Frame] = None

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

    def set_logo_image(self, bg_color: Literal["blue", "red"]) -> None:
        image = tk.PhotoImage(file=self.paths[f"file_logo_{bg_color}"]) # type:ignore
        logo = tk.Label(self.current_frame, image=image, borderwidth=0, highlightthickness=0)
        logo.image = image
        logo.pack()

    def set_normal_mode_button(self, fct: Callable) -> None:
        normal_mode_button = tk.Button(
            self.current_frame, text="Partie classique", font=self.font("text"), command=fct)
        normal_mode_button.pack()

    def set_competitive_mode_button(self) -> None:
        competitive_mode_button = tk.Button(
            self.current_frame, text="Partie compétitive", font=self.font("text"), command=self.play_quiz_competitive)
        competitive_mode_button.pack()

    def set_chapter_button(self) -> None:
        chapter_button = tk.Button(self.current_frame, text="Sélection des chapitres",
                                   font=self.font("text"), command=lambda: self.setup_fenetre("chapter", chapter=self.chapters))
        chapter_button.pack()

    def set_parameter_button(self) -> None:
        parameter_button = tk.Button(self.current_frame, text="Paramètres", font=self.font(
            "text"), command=lambda: self.setup_fenetre("parameter"))
        parameter_button.pack()

    """___Chapters___"""

    def set_home_button(self) -> None:
        home_button = tk.Button(self.current_frame, text="Menu",
                                font=self.font("text"), command=lambda: self.setup_fenetre("home"))
        home_button.pack()

    def set_chapters_boxes(self, chapters: Dict[str, tk.BooleanVar]) -> None:
        chapter_boxes = []
        for chapter, check in chapters.items():
            if not isinstance(check, tk.BooleanVar):    # First launch
                chapters[chapter] = tk.BooleanVar(value=True)
            chapter_boxes.append(tk.Checkbutton(
                self.current_frame, text=chapter, font=self.font("small"), variable=chapters[chapter]))
            chapter_boxes[-1].pack()

    def set_scroll_bar(self) -> None:
        """
        Work in progress
        """
        canvas = tk.Canvas(self.current_frame)
        scroll_bar = tk.Scrollbar(
            self.current_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        self.current_frame = tk.Frame(canvas, bg=self.color_BG_menu)
        canvas.create_window((0, 0), window=self.current_frame, anchor="nw")
        self.current_frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))

    """___Parameter___"""

    def set_increase_font_size_button(self) -> None:
        increase_font_size_button = tk.Button(self.current_frame, text="Augmenter la taille de police", font=self.font(
            "text"), command=self.increase_font_size)
        increase_font_size_button.pack()

    def set_decrease_font_size_button(self) -> None:
        decrease_font_size_button = tk.Button(self.current_frame, text="Diminuer la taille de police", font=self.font(
            "text"), command=self.decrease_font_size)
        decrease_font_size_button.pack()

    def increase_font_size(self) -> None:
        self.font_size_buff += 0.1
        self.setup_fenetre("parameter")

    def decrease_font_size(self) -> None:
        self.font_size_buff = max(0.4, self.font_size_buff-0.1)
        self.setup_fenetre("parameter")

    """___Quiz___"""

    def set_question_label(self, message: str) -> None:
        self.question_label = tk.Label(
            self.current_frame, text=message, font=self.font("text"))
        self.question_label.pack(pady=30)

    def reset_question_label(self, message: str) -> None:
        self.question_label.config(text=message)

    def set_guess_entry(self) -> None:
        self.guess_entry = tk.Entry(
            self.current_frame, width=60, font=self.font("text"))
        self.guess_entry.pack()
        self.guess_entry.focus_set()

    def reset_guess_entry(self) -> None:
        self.guess_entry.delete(0, tk.END)

    def set_validation_button(self, action: Callable = lambda: 1+1) -> None:
        self.validation_button = tk.Button(
            self.current_frame, text="Valider", font=self.font("text"), command=action)
        self.validation_button.pack(pady=30)

    def reset_validation_button(self, action: Callable = lambda: 1+1) -> None:
        self.validation_button.config(command=action)

    def set_question_result_label(self, message: str) -> None:
        self.question_result_label = tk.Label(
            self.current_frame, text=message, font=self.font("text"))
        self.question_result_label.pack()

    def reset_question_result_label(self, message: str) -> None:
        self.question_result_label.config(text=message)

    """___Results___"""

    def set_conclusion_label(self) -> None:
        conclusion_label = tk.Label(
            self.current_frame, text="", font=self.font("text"))
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

        conclusion_label.config(text=text)
        conclusion_label.pack()

    def set_score_label(self) -> None:
        score = int(np.sum(self.quiz_results))
        if score == len(self.quiz_results):
            displayed_score = "Score Parfait !"
        elif score == 0:
            displayed_score = "Score horrible !"
        else:
            displayed_score = f"Score : {score}/{len(self.quiz_results)}"
        score_label = tk.Label(
            self.current_frame, text=displayed_score, font=self.font("text"))
        score_label.pack()

    def set_timer_label(self) -> None:
        timer_label = tk.Label(
            self.current_frame, text=f"Temps : {round(self.quiz_time, 2)}s", font=self.font("text"))
        timer_label.pack()

    def set_replay_button(self) -> None:
        replay_button = tk.Button(
            self.current_frame, text="Rejouer", font=self.font("text"), command=self.play_quiz)
        replay_button.pack()

    def set_quit_button(self) -> None:
        quit_button = tk.Button(
            self.current_frame, text="Quitter", font=self.font("text"), command=self.kill_fenetre)
        quit_button.pack()
