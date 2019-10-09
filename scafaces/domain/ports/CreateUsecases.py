from abc import ABCMeta, abstractmethod
from scafaces.domain.models.People import People


class CreateUsecases(metaclass=ABCMeta):

    @abstractmethod
    def create(self, data: People):
        raise NotImplementedError("detector must define create method")

    @abstractmethod
    def recognizer(self):
        raise NotImplementedError("detector must define recognizer method")