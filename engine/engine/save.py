"""___Modules_______________________________________________________________"""

# bwizz
from ..utils import *
from .fenetre import Fenetre

# Python
import numpy as np
from typing import Dict, List, Tuple

"""___Classes_______________________________________________________________"""


class Save(Fenetre):

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

    def reset_save(self) -> None:
        save_elements = [element for element, _, _ in self.save]
        for element in save_elements:
            self.scores[element] = 0
            self.attempts[element] = 0
        self.erase_save()

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
        self.write_txt(self.paths["file_save"], save[:-1], extension="")
