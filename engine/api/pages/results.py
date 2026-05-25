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

    with ui.column().classes("items-center justify-center w-full h-screen gap-4"):
        ui.label("Résutlats").classes("text-4xl font-bold")

        ui.button("Home 🏠", on_click=ui.navigate.to("/"))
