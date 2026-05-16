"""___Modules___________________________________________________________________________________"""

# bwizz
from ..engine import Engine

# Python
from nicegui import app, ui
from typing import Optional

"""___Functions_________________________________________________________________________________"""

def create(engine: Engine) -> None:
    # Logo
    ui.image(engine.paths["file_logo_blue"])
    # Question
    question_label = ui.label(engine.active_question)
    # Barre de texte
    guess_entry = ui.input(label="Votre réponse", placeholder="Entrez votre réponse ici")
    # Bouton de validation
    validation_button = ui.button("Valider", on_click=lambda: valider(engine, guess_entry.value))
    # Texte du résultat
    result_label = ui.label("")
    # Binds
    guess_entry.on("keydown.enter", lambda: valider(engine, guess_entry.value))

    def valider(engine: Engine, guess: Optional[str]) -> None:
        engine.valider(guess)
        result_label.set_text(engine.result_label)
