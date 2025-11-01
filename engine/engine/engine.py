"""___Modules_______________________________________________________________"""

# Quiz
from ..utils import *
from .interface import Fenetre

# Python
import numpy as np

"""___Classes_______________________________________________________________"""


class Engine(Fenetre):

    def start(self) -> None:
        self.import_data()
        self.import_save()

    def import_data(self) -> None:
        self.data = self.import_data_file()
        self.elements = list(self.data.keys())

    def import_save(self) -> None:
        self.save = self.import_save_file()
        self.scores = {}
        self.attempts = {}

        # No save
        if self.save == []:
            pass
        
        # Save exists
        else:
            for element, score, attempt in self.save:
                self.scores[element] = score
                self.attempts[element] = attempt
        
        self.fix_save()
    
    def fix_save(self) -> None:
        save_elements = [element for element, _, _ in self.save]
        for element in self.elements:
            if element not in save_elements:
                self.scores[element] = 0
                self.attempts[element] = 0

    def erase_save(self) -> None:
        save = ""
        for element in self.elements:
            save += f"{element}:{self.scores[element]}:{self.attempts[element]}\n"
        self.write_txt(self.paths["save"], save[:-1], extension="bw")

    def get_questions(self, duree: int) -> list:
        lenE = len(self.elements)
        if len(self.elements) <= duree:
            return self.elements
        indexes = []
        questions = []
        for _ in range(duree):
            index = np.random.randint(0, lenE)
            while index in indexes:
                index = np.random.randint(0, lenE)
            indexes.append(index)
            questions.append(self.elements[index])

        return questions

    def quizz(self, duree: int = 3) -> None:
        self.init_fenetre()
        self.init_quiz(self.get_questions(duree))

        self.questionner()
        self.start_fenetre()

        print(self.get_results())
