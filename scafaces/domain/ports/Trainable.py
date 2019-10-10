from abc import ABCMeta, abstractmethod
from typing import NoReturn


class Trainable(metaclass=ABCMeta):

    @abstractmethod
    def recognizer(self) -> NoReturn:
        raise NotImplementedError("train model must define recognizer method")