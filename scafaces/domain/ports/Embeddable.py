from abc import ABCMeta, abstractmethod
from scafaces.domain.models.People import People


class Embeddable(metaclass=ABCMeta):

    @abstractmethod
    def read(self):
        raise NotImplementedError("detector must define read method")

    @abstractmethod
    def create(self, data: People):
        raise NotImplementedError("detector must define createEmbeddings method")