"""___Modules___________________________________________________________________________________"""

# bwizz
from ..engine import Engine

# Python
from nicegui import app, ui

"""___Functions_________________________________________________________________________________"""

def create(engine: Engine) -> None:
    # Logo
    ui.image(engine.paths["file_logo_blue"])
    # Conclusion
    ui.label("Merci d'avoir joué !").classes("text-center")
    # Score
    ui.label(f"Votre score : {engine.score} / {engine.quiz_length}").classes("text-center")
    # Chrono
    ui.label(f"Temps : {engine.quiz_time}").classes("text-center")
    # Home
    ui.button("Accueil", on_click=lambda: ui.navigate.to("/home")).classes("text-center")
    # Binds
    ui.on("keydown.m", lambda: ui.navigate.to("/"))
    ui.on("keydown.r", engine.setup_quiz)
