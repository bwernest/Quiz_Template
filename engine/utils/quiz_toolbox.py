"""___Modules_______________________________________________________________"""

# bwizz
from .errors import *
from .toolbox import ToolBox

# Python
import json
from time import perf_counter as clock
from tkinter import BooleanVar
from typing import Dict, List, Tuple

"""___Functions_____________________________________________________________"""


class QuizToolBox(ToolBox):

    chapters: Dict[str, BooleanVar]

    def init_chapters(self) -> None:
        self.chapters = {}

    def import_data_file(self) -> Dict[str, Dict[str, str]]:
        try:
            raw_data: Dict[str, Dict[str, str]] = json.load(
                open(self.paths["file_data"], encoding="utf-8"))
            data = {}
            for chapter in raw_data.keys():
                data[chapter] = {}
                for sigle, meaning in raw_data[chapter].items():
                    data[chapter][sigle] = meaning
            return data
        except QuizDataUnreadable:
            raise QuizDataUnreadable()

    def normalize_string(self, string: str) -> str:
        conversion = {"à": "a", "â": "a",
                      "é": "e", "è": "e", "ê": "e",
                      "î": "i",
                      "ô": "o",
                      "ù": "u", "û": "u",
                      "-": "", " ": "", ",": "", "'": ""
                      }
        new_string = string.lower()
        final_string = ""
        for letter in new_string:
            if letter in conversion:
                final_string += conversion[letter]
            else:
                final_string += letter
        return final_string

    def import_save_file(self) -> List:
        try:
            raw_save = self.read_txt(self.paths["file_save"]).split("\n")
            save = []
            for l, line in enumerate(raw_save):
                QA = line.split(":")
                save.append([QA[0], eval(QA[1]), eval(QA[2])])
            return save
        except QuizSaveUnreadable:
            raise QuizSaveUnreadable()

    def answer_is_correct(self, guess: str, answer: str) -> bool:
        return self.normalize_string(guess) == self.normalize_string(answer)

    def start_timer(self) -> None:
        self.quiz_time = clock()

    def end_timer(self) -> None:
        self.quiz_time = clock() - self.quiz_time
