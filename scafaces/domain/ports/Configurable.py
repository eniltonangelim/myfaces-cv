from abc import ABCMeta, abstractmethod
from scafaces.domain.ports.FindUsecases import FindUsecases
from scafaces.domain.ports.CreateUsecases import CreateUsecases


class Configurable(metaclass=ABCMeta):

    @abstractmethod
    def getFindEmbedded(self) -> FindUsecases:
        raise NotImplementedError("configuration must define getEmbedded method")

    @abstractmethod
    def getFindDetector(self) -> FindUsecases:
        raise NotImplementedError("configuration must define getDetector method")

    @abstractmethod
    def getFindImages(self) -> FindUsecases:
        raise NotImplementedError("configuration must define getImages method")

    @abstractmethod
    def getCreateEmbedded(self) -> CreateUsecases:
        raise NotImplementedError("configuration must define getCreateEmbedded method")

    @abstractmethod
    def getTrain(self) -> CreateUsecases:
        raise NotImplementedError("configuration must define getTrain method")

