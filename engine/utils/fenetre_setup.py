"""___Modules_______________________________________________________________"""

# bwizz
from .fenetre_build import FenetreBuilder

# Python
from nicegui import app, ui
import numpy as np

"""___Classes_______________________________________________________________"""


class FenetreSetup(FenetreBuilder):

    def setup_fenetre_home(self, **kwargs) -> None:
        # Logo
        ui.label("Quiz Game")
        ui.image(self.paths["file_logo_blue"])
        # Normal
        ui.button("Partie Classique", on_click=kwargs["normal_mode_button"])
        # Compétitif
        ui.button("Partie Compétitive", on_click=kwargs["competitive_mode_button"])
        # Bouton paramètres
        ui.button("Paramètres", on_click=lambda: self.setup_fenetre("parameter"))
        # Bouton Quitter
        ui.button("Quitter", on_click=app.shutdown)
        app.on_shutdown(lambda: print("Fermeture de l'application..."))

    def setup_fenetre_quiz(self, **kwargs) -> None:
        # Logo
        ui.image(self.paths["file_logo_blue"])
        # Question
        self.set_question_label("")
        # Barre de texte
        self.set_guess_entry()
        # Bouton de validation
        self.set_validation_button(self.valider)
        # Texte du résultat
        self.set_question_result_label("")
        # Binds
        self.guess_entry.on("keydown.enter", self.valider)

    def setup_fenetre_conclusion(self, **kwargs) -> None:
        # Logo
        ui.image(self.paths["file_logo_blue"])
        # Conclusion
        self.set_conclusion_label()
        # Score
        self.set_score_label()
        # Chrono
        self.set_timer_label()
        # Home
        self.set_home_button()
        # Binds
        ui.on("keydown.m", self.setup_fenetre("home"))
        ui.on("keydown.r", self.play_quiz)

    def setup_fenetre_parameter(self, **kwargs) -> None:
        # Logo
        ui.image(self.paths["file_logo_blue"])
        # Font size
        self.set_increase_font_size_button()
        self.set_decrease_font_size_button()
        # Retour
        self.set_home_button()
