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
    engine.set_conclusion_label()
    # Score
    engine.set_score_label()
    # Chrono
    engine.set_timer_label()
    # Home
    engine.set_home_button()
    # Binds
    ui.on("keydown.m", lambda: ui.navigate.to("/home"))
    ui.on("keydown.r", engine.setup_quiz)
