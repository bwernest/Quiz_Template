"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ...engine.engine import Engine

# Python
import asyncio
from nicegui import app, ui

"""___Fonctions_________________________________________________________________________________"""

def create(engine: Engine) -> None:

    def start_game() -> None:
        engine.setup_game()
        ui.navigate.to("/play")
    
    async def quitter() -> None:
        titre_label.set_text("Connard")
        await asyncio.sleep(1)
        app.shutdown()

    with ui.column().classes("items-center justify-center w-full h-screen gap-4"):
        titre_label = ui.label("🧠 ❓ Bienvenue dans bwiz 📝 🤔").classes("text-4xl font-bold")

        ui.button("Jouer 🕹️", on_click=start_game)

        ui.button("Quitter 🥲", on_click=quitter)
