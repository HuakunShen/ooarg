from typing import List
from abc import ABC, abstractmethod

from ooarg.src.command.arg import Arg


class Command(ABC):
    examples: List[str]
    flags: List[Arg]
    args: List[Arg]

    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        raise NotImplementedError
