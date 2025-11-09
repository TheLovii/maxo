from enum import Enum


class Sentinels(Enum):
    UNHANDLED = "<unhandled>"
    REJECTED = "<rejected>"


UNHANDLED = Sentinels.UNHANDLED
REJECTED = Sentinels.REJECTED
