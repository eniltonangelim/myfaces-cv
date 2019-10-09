from abc import ABCMeta, abstractmethod


class FindUsecases(metaclass=ABCMeta):

    @abstractmethod
    def read(self):
        raise NotImplementedError("detector must define read method")