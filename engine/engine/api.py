"""___Modules___________________________________________________________________________________"""

# bwizz
from .pages import home, parameter, play
from .engine import Engine

# Python
from nicegui import ui

"""___Functions___________________________________________________________________________________"""

engine = Engine()
engine.start()

@ui.page("/")
def home_page():
    home.create(engine)

@ui.page("/play")
def play_page():
    play.create(engine)

@ui.page("/parameter")
def parameter_page():
    parameter.create(engine)

ui.run(title="bwizz", dark=True)
