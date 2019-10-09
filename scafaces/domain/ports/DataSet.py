from abc import ABCMeta, abstractmethod
from typing import List


class DataSet(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self):
        raise NotImplementedError("dataset must define get_name method")

    @abstractmethod
    def get_path(self):
        raise NotImplementedError("dataset must define get_name method")

    @abstractmethod
    def getImages(self) -> List[str]:
        raise NotImplementedError("dataset must define getImages method")