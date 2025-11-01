"""___Modules_______________________________________________________________"""

# Quiz
from ..utils import *

# Python
import tkinter as tk

"""___Classes_______________________________________________________________"""


class Fenetre(ToolBox):

    def init_fenetre(self) -> None:
        self.fenetre = tk.Tk()
        self.fenetre.geometry("500x500")
        self.fenetre.title("O'sigle")

        # Logo
        image = tk.PhotoImage(file=self.paths["logo"])
        self.logo = tk.Label(self.fenetre, image=image)
        self.logo.image = image
        self.logo.pack()

        # Question
        self.question = tk.Label(self.fenetre, text="", font=("Times", 18))
        self.question.pack(pady=30)

        # Barre de texte
        self.entree = tk.Entry(self.fenetre, width=60)
        self.entree.pack()

        # Bouton de validation
        self.bouton = tk.Button(self.fenetre, text="Valider", font=(
            "Times", 18), command=self.valider)
        self.bouton.pack(pady=30)

        # Texte du résultat
        self.result_label = tk.Label(self.fenetre, text="", font=("Times", 18))
        self.result_label.pack()

        # Binds
        self.fenetre.bind("<Return>", self.valider)
        self.fenetre.bind("<Escape>", self.kill_fenetre)

    def init_quiz(self, questions: list, answers: list) -> None:
        self.questions = questions
        self.answers = answers
        self.guesses = []
        self.reset_question_index()

    def start_fenetre(self) -> None:
        self.fenetre.mainloop()

    def questionner(self) -> None:
        self.result_label.config(text="")
        index = self.get_question_index
        if index < len(self.questions):
            self.question.config(
                text=f"Que signifie {self.questions[index]} ?")
            self.entree.delete(0, tk.END)
        else:
            self.kill_fenetre()

    def reset_question_index(self) -> None:
        self.question_index = -1

    @property
    def get_question_index(self) -> int:
        self.question_index += 1
        return self.question_index

    def valider(self, event=None) -> None:
        guess = self.entree.get()
        self.guesses.append(guess)
        if guess == self.answers[self.question_index]:
            shift = 0
        else:
            self.result_label.config(text="SAC A MERDE")
            shift = 1500
        self.fenetre.after(shift, self.questionner)

    def get_results(self) -> list:
        results = [guess == answer for guess, answer in zip(self.guesses, self.answers)]
        return results

    def kill_fenetre(self, envent=None) -> None:
        self.fenetre.destroy()
