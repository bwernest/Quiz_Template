"""___Modules___________________________________________________________________________________"""

# bwizz
from ..engine import Engine

# Python
from nicegui import app, ui

"""___Functions_________________________________________________________________________________"""

def create(engine: Engine) -> None:
    # Logo
    ui.label("Quiz Game")
    ui.image(engine.paths["file_logo_blue"])
    # Normal
    ui.button("Partie Classique", on_click=lambda: go_play(engine))
    # Compétitif
    ui.button("Partie Compétitive", on_click=lambda: go_play_competitive(engine))
    # Bouton paramètres
    ui.button("Paramètres", on_click=lambda: ui.navigate.to("/parameter"))
    # Bouton Quitter
    ui.button("Quitter", on_click=app.shutdown)
    app.on_shutdown(lambda: print("Fermeture de l'application..."))

def go_play(engine: Engine) -> None:
    engine.setup_quiz()
    engine.questionner()
    ui.navigate.to("/play")

def go_play_competitive(engine: Engine) -> None:
    engine.play_quiz_competitive()
    ui.navigate.to("/play")
