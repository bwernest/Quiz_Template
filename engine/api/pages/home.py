"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ...engine.engine import Engine

# Python
from nicegui import app, ui

"""___Fonctions_________________________________________________________________________________"""

def create(engine) -> None:
    
    with ui.column().classes("items-center justify-center w-full h-screen gap-4"):
        ui.label("🧠 ❓ Bienvenue dans QuizTempalte 📝 🤔").classes("text-4xl font-bold")

        ui.button("Jouer 🕹️", on_click=lambda: ui.navigate.to("/play"))

        ui.button("Quitter 🥲")
