"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ...engine.engine import Engine
from ...utils import *

# Python
from nicegui import app, ui

"""___Fonctions_________________________________________________________________________________"""

def create(engine: Engine) -> None:
    
    def valider() -> None:
        guess_entry.on("keydown.enter", lambda: None)
        engine.give_answer(guess_entry.value)  # type:ignore
        update_page()
    
    def update_page() -> None:
        question_label.set_text(engine.active_question)
        correction_label.set_text(engine.active_correction)

    with ui.column().classes("items-center justify-center w-full h-screen gap-4"):
        ui.label("👾 QuizTempalte 👾").classes("text-4xl font-bold")

        question_label = ui.label(engine.active_question)
        guess_entry = ui.input(placeholder=engine.active_guess_entry, value="")
        guess_entry.on("keydown.enter", valider)
        correction_label = ui.label(engine.active_correction)

        ui.button("Valider ✅", on_click=valider)
