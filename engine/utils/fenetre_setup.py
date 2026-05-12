"""___Modules_______________________________________________________________"""

# bwizz
from .fenetre_build import FenetreBuilder

# Python
import numpy as np
import tkinter as tk

"""___Classes_______________________________________________________________"""


class FenetreSetup(FenetreBuilder):

    def clear_frame(self) -> None:
        if self.current_frame is not None:
            self.current_frame.destroy()

    def setup_fenetre_home(self, **kwargs) -> None:
        # Logo
        self.set_logo_image("blue")
        # Normal
        self.set_normal_mode_button(kwargs["normal_mode_button"])
        # Compétitif
        self.set_competitive_mode_button()
        # Bouton Chapitres
        self.set_chapter_button()
        # Bouton paramètres
        self.set_parameter_button()
        # Bouton Quitter
        self.set_quit_button()

    def setup_fenetre_quiz(self, **kwargs) -> None:
        # Logo
        self.set_logo_image(kwargs["bg_color"])
        # Question
        self.set_question_label("")
        # Barre de texte
        self.set_guess_entry()
        # Bouton de validation
        self.set_validation_button(self.valider)
        # Texte du résultat
        self.set_question_result_label("")
        # Binds
        self.main_fenetre.bind("<Return>", self.valider)

    def setup_fenetre_conclusion(self, **kwargs) -> None:
        # Logo
        self.set_logo_image("blue")
        # Conclusion
        self.set_conclusion_label()
        # Score
        self.set_score_label()
        # Chrono
        self.set_timer_label()
        # Home
        self.set_home_button()
        # Binds
        self.main_fenetre.bind("<m>", self.setup_fenetre_home)
        self.main_fenetre.bind("<r>", self.play_quiz)

    def setup_fenetre_chapter(self, **kwargs) -> None:
        # Logo
        self.set_logo_image("blue")
        # Chapitres
        self.set_chapters_boxes(kwargs["chapters"])
        # Retour
        self.set_home_button()

    def setup_fenetre_parameter(self, **kwargs) -> None:
        # Logo
        self.set_logo_image("blue")
        # Font size
        self.set_increase_font_size_button()
        self.set_decrease_font_size_button()
        # Retour
        self.set_home_button()
