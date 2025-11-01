"""___Modules_______________________________________________________________"""

# Quiz
from .settings import Settings

# Python
import os
import datetime
import pandas as pd
from typing import Dict, List

"""___Functions_____________________________________________________________"""


class ToolBox(Settings):

    def write_txt(self, path: str, text: str, append: bool = False, extension: str = "txt") -> None:
        if append:
            method = "a"
        else:
            method = "w"
        if "/" in path:
            SplitPath = path.split("/")
            os.makedirs("/".join(SplitPath[:-1]), exist_ok=True)
        txt = open(f"{path}.{extension}", method, encoding="utf-8")
        txt.write(text)
        txt.close()

    def read_txt(self, path: str) -> str:
        txt = open(path, "r", encoding="utf-8", errors="ignore")
        data = txt.read()
        txt.close()
        return data

    def export_txt(self, txt: str, title: str = "DebugExport") -> None:
        self.write_txt(f"{title}", txt)

    def print_info(self, text: str, object: any, option: str = "") -> None:
        """
        Print function. Option available : liste -> displays object line by line.
        """
        if option == "":
            print(f"{text} ({type(object)})\t: {object}")
        elif option == "liste":
            if isinstance(object, list):
                for data in object:
                    self.print_info(text, data)
            elif isinstance(object, dict):
                self.print_info(text, "")
                for key, value in object.items():
                    self.print_info(key, value)
            else:
                raise ValueError(
                    f"Asking to show an object like an iterable but got : {type(object)}.")
        elif option == "token":
            self.print_info(text, f"{object.type} / {object.value}")

    def add_log(self, text: str, objects: Dict[str, any] = {}, time: bool = True, disp: bool = True) -> None:
        if objects == {}:
            log = f"{text}"
        else:
            log = f"{text} : {objects}"
        if time:
            now = f"[{datetime.datetime.now().strftime("%d/%m/%Y-%H:%M")}]"
            log = f"{now} - {log}"
        self.write_txt("log", log+"\n", append=True)
        if disp:
            print(log)

    def del_log(self):
        self.write_txt("log", "")

    def get_local_files(self, path: str) -> List[str]:
        return os.listdir(path)

    def delete(self, path: str) -> None:
        os.remove(path)

    def search_format(self, format: str, path: str) -> list[str]:
        files = []
        lenF = len(format)
        for file in os.listdir(path):
            if os.path.isfile(path+"/"+file):
                if len(file) > lenF and file[-lenF:] == format:
                    files.append(path+"/"+file)
            else:
                files += self.search_format(format, path+"/"+file)
        return files

    def clean_folder(self, path: str, subcall: bool = False) -> None:
        if os.path.exists(path):
            files = os.listdir(path)
            for file in files:
                if "." in file:
                    os.remove(f"{path}/{file}")
                else:
                    self.clean_folder(f"{path}/{file}", subcall=True)
            if subcall:
                os.rmdir(path)

    def import_data_file(self) -> dict:
        raw_data = pd.read_excel(self.paths["data"]).to_dict()
        sigles = []
        data = {}
        for sigle in raw_data["Question"].values():
            sigles.append(sigle)
        for key, signification in raw_data["Réponse"].items():
            data[sigles[key]] = str(signification)
        return data

    def import_save_file(self) -> dict:
        raw_save = self.read_txt(self.paths["save"]).split("\n")
        for l, line in enumerate(raw_save):
            raw_save[l] = line.split(":")
            raw_save[l][1] = eval(raw_save[l][1])
            raw_save[l][2] = eval(raw_save[l][2])
        return raw_save
