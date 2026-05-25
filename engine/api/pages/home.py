"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ...engine.engine import Engine

# Python
from nicegui import app, ui

"""___Fonctions_________________________________________________________________________________"""

def create(engine: Engine) -> None:

    def start_game() -> None:
        engine.setup_game()
        ui.navigate.to("/play")
    
    with ui.column().classes("items-center justify-center w-full h-screen gap-4"):
        ui.label("🧠 ❓ Bienvenue dans bwiz 📝 🤔").classes("text-4xl font-bold")

        ui.button("Jouer 🕹️", on_click=start_game)

        ui.button("Quitter 🥲")
