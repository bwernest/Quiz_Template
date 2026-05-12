"""___Classes_______________________________________________________________"""


class QuizException(Exception):
    pass


class SettingsNotAvailable(QuizException):
    pass


class QuizDataUnreadable(QuizException):
    pass


class QuizSaveUnreadable(QuizException):
    pass
