from abc import ABCMeta, abstractmethod
from scafaces.domain.models.People import People
from typing import List


class Detectable(metaclass=ABCMeta):

    @abstractmethod
    def read(self):
        raise NotImplementedError("detector must define read method")

    @abstractmethod
    def detector(self, images: List[str], embedder = None) -> People:
        raise NotImplementedError("detector must define detector method")