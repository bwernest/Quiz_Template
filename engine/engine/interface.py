"""___Modules_______________________________________________________________"""

# Osigle
from ..utils import *

# Python
import tkinter as tk

"""___Classes_______________________________________________________________"""


class Fenetre(ToolBox):

    def init_fenetre(self) -> None:
        self.fenetre = tk.Tk()
        self.fenetre.geometry("500x400")
        self.fenetre.title("O'sigle")

        image = tk.PhotoImage(file=self.paths["logo"])
        self.logo = tk.Label(self.fenetre, image=image)
        self.logo.image = image
        self.logo.pack()

        self.question = tk.Label(self.fenetre, text="", font=("Times", 18))
        self.question.pack(pady=30)

        self.entree = tk.Entry(self.fenetre, width=60)
        self.entree.pack()

        self.bouton = tk.Button(self.fenetre, text="Valider", font=(
            "Times", 18), command=self.valider)
        self.bouton.pack(pady=30)

        self.fenetre.bind("<Return>", self.valider)
        self.fenetre.bind("<Escape>", self.kill_fenetre)

    def init_quiz(self, questions: list) -> None:
        self.questions = questions
        self.reponses = []
        self.reset_question_index()

    def start_fenetre(self) -> None:
        self.fenetre.mainloop()

    def questionner(self) -> None:
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
        self.reponses.append(self.entree.get())
        self.fenetre.after(0, self.questionner)

    def get_results(self) -> list:
        return self.reponses

    def kill_fenetre(self, envent=None) -> None:
        self.fenetre.destroy()
