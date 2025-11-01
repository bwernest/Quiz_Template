"""___Modules_______________________________________________________________"""

# Quiz
from .errors import *

# Python
import json

"""___Classes_______________________________________________________________"""


class Settings():

    _config = None

    # Settings
    paths: list
    test: bool

    def __init__(self, category: str = "prod") -> None:
        if Settings._config is None:

            with open("engine/settings.json") as file:
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
        except KeyError:
            raise SettingsNotAvailable(
                f"Paramètres {category} inexistants ou non répertoriés.")
