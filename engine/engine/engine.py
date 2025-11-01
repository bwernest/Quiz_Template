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
        self.write_txt(self.paths["save"], save[:-1], extension="")

    def get_questions(self, duree: int) -> tuple[list, list]:
        lenE = len(self.elements)
        if len(self.elements) <= duree:
            return self.elements
        indexes = []
        questions = []

        # Liste pondérée des indices
        ponderated_indexes = []
        for index in range(lenE):
            score = self.scores[self.elements[index]]
            attempt = self.attempts[self.elements[index]]
            ponderated_indexes.extend([index]*int(attempt-score+1))
        lenP = len(ponderated_indexes)

        # Tirage des questions
        for _ in range(duree):
            index = np.random.randint(0, lenP)
            while ponderated_indexes[index] in indexes:
                lenP -= 1
                ponderated_indexes.pop(index)
                index = np.random.randint(0, lenP)
            indexes.append(ponderated_indexes[index])
            ponderated_indexes.pop(index)
            lenP-=1
            questions.append(self.elements[indexes[-1]])
            self.attempts[questions[-1]] += 1

        # Réponses
        answers = []
        for element in questions:
            answers.append(self.data[element])

        return questions, answers

    def quizz(self, duree: int = 3) -> None:
        self.init_fenetre()
        questions, answers = self.get_questions(duree)
        self.init_quiz(questions, answers)

        self.questionner()
        self.start_fenetre()

        results = self.get_results()
        for r, result in enumerate(results):
            if result:
                element = questions[r]
                self.scores[element] += 1

        self.erase_save()
