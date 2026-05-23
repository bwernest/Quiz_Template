"""___Modules___________________________________________________________________________________"""

# bwizz
from ..engine import Engine

# Python
import asyncio
from nicegui import app, ui
from typing import Optional

"""___Functions_________________________________________________________________________________"""

def create(engine: Engine) -> None:
    engine.add_log("Création de play page")
    # Logo
    ui.image(engine.paths["file_logo_blue"])
    # Question
    question_label = ui.label(engine.active_question).classes("text-center")
    # Barre de texte
    guess_entry = ui.input(label="Votre réponse", placeholder="Entrez votre réponse ici").classes("text-center")
    # Bouton de validation
    validation_button = ui.button("Valider", on_click=lambda: valider()).classes("text-center")
    # Texte du résultat
    result_label = ui.label(text="").classes("text-center")
    # Binds
    guess_entry.on("keydown.enter", lambda: valider())

    async def valider() -> None:
        guess_entry.on("keydown.enter", lambda: None)
        engine.valider(guess_entry.value)

        result_label.set_text(engine.result_label)
        
        print("Réponse donnée")
        await asyncio.sleep(engine.time_after_answer)
        print("Next question")
        next_question()

    def next_question() -> None:
        if engine.question_index < engine.quiz_length:
            engine.questionner()
            question_label.set_text(engine.active_question)
            guess_entry.set_value("")
            validation_button.set_text(f"Valider {engine.question_index}")
            result_label.set_text("")
            guess_entry.on("keydown.enter", lambda: valider())
        else:
            engine.end_quiz()
            ui.navigate.to("/conclusion")
