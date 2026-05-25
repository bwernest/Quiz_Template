"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ...engine.engine import Engine
from ...utils import *

# Python
import asyncio
from time import sleep
from tqdm import tqdm
from nicegui import app, ui

"""___Fonctions_________________________________________________________________________________"""

def create(engine: Engine) -> None:
    
    async def valider() -> None:
        guess_entry.on("keydown.enter", lambda: None)
        engine.give_answer(guess_entry.value)  # type:ignore
        update_page()
        for _ in tqdm(range(100)):
            await asyncio.sleep(0.02)
        next_question()
    
    def next_question():
        engine.go_next_question()
        if engine.active_question_index == engine.quiz_length:
            ui.navigate.to("/results")
        else:
            update_page()
            guess_entry.set_value("")
            guess_entry.on("keydown.enter", valider)
    
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
