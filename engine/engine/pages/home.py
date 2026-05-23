"""___Modules___________________________________________________________________________________"""

# bwizz
from ..engine import Engine

# Python
from nicegui import app, ui

"""___Functions_________________________________________________________________________________"""

def create(engine: Engine) -> None:
    engine.add_log("Création de home page")
    # Logo
    ui.label("Quiz Game").classes("text-center")
    ui.image(engine.paths["file_logo_blue"]).classes("text-center")
    # Normal
    ui.button("Partie Classique", on_click=lambda: go_play(engine)).classes("text-center")
    # Compétitif
    ui.button("Partie Compétitive", on_click=lambda: go_play_competitive(engine)).classes("text-center")
    # Bouton paramètres
    ui.button("Paramètres", on_click=lambda: ui.navigate.to("/parameter")).classes("text-center")
    # Bouton Quitter
    ui.button("Quitter", on_click=app.shutdown).classes("text-center")
    app.on_shutdown(lambda: print("Fermeture de l'application..."))

def go_play(engine: Engine) -> None:
    engine.setup_quiz()
    engine.questionner()
    ui.navigate.to("/play")

def go_play_competitive(engine: Engine) -> None:
    engine.play_quiz_competitive()
    ui.navigate.to("/play")
