"""___Modules___________________________________________________________________________________"""

# QuizTemplate
from ..engine.engine import Engine
from .pages import home, play

# Python
from nicegui import app, ui

"""___Classes___________________________________________________________________________________"""

class QuizTemplate():

    def __init__(self, category: str) -> None:
        self.engine = Engine(category)
        self.engine.add_log("Démarrage du moteur")
        self.engine.start()
        self.engine.add_log("Création des pages")
        self.create_pages()
    
    def create_pages(self) -> None:
        
        @ui.page("/")
        def page_home():
            self.engine.add_log("Création de la page home")
            home.create(self.engine)

        @ui.page("/play")
        def page_play():
            self.engine.add_log("Création de la page play")
            play.create(self.engine)

    def start(self) -> None:
        self.engine.add_log("Démarrage de l'interface")
        ui.run(title="Quiz Template")
