"""___Modules___________________________________________________________________________________"""

# bwizz
from ..engine import Engine

# Python
from nicegui import app, ui

"""___Functions_________________________________________________________________________________"""

def create(engine: Engine) -> None:
    engine.add_log("Création de parameter page")
    # Logo
    ui.image(engine.paths["file_logo_blue"])
    # Font size
    engine.set_increase_font_size_button()
    engine.set_decrease_font_size_button()
    # Retour
    engine.set_home_button()
