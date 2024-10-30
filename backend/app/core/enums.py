import random
from enum import Enum


class SubjectEnum(Enum):
    MATH = "Math"
    SCIENCE = "Science"
    HISTORY = "History"
    ART = "Art"

    @classmethod
    def random(cls):
        return random.choice(list(cls))


def random_subject():
    return SubjectEnum.random().value
