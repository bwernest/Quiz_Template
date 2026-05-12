"""___Modules_______________________________________________________________"""

# bwizz
from .errors import *

# Python
import json
import os
from typing import Dict, List, Literal, Tuple

"""___Classes_______________________________________________________________"""


class Settings():

    _config = None

    # Settings
    paths: Dict[Literal[
        "file_data",
        "file_save",
        "file_logo",
        "file_logo_blue",
        "file_logo_red",
    ], str]
    test: bool
    _paths_updated: List = []

    normal_mode_length: int
    competitive_mode_length: int

    window_title: str
    window_size: Tuple[int, int]

    color_BG_menu: str
    color_BG_competitive: str

    font_type: str
    font_size_title: int
    font_size_text: int
    font_size_small: int

    def __init__(self, category: str = "prod") -> None:
        dirname = os.path.dirname(__file__)
        if Settings._config is None:

            settings_path = os.path.join(dirname, "../settings.json")
            with open(settings_path) as file:
                Settings._config = json.load(file)

        # Paramètres universels
        self.category = category
        for key, value in Settings._config.items():
            if not isinstance(value, dict):
                setattr(self, key, value)

        # Paramètres de configuration
        try:
            for key, value in Settings._config[category].items():
                setattr(self, key, value)
            # Update des paths
            for path_key in set(self.paths.keys()) - set(self._paths_updated):
                self.paths[path_key] = os.path.join(dirname, f"../../{self.paths[path_key]}")
                self._paths_updated.append(path_key)
        except KeyError:
            raise SettingsNotAvailable(f"Paramètres {category} inexistants ou non répertoriés.")
