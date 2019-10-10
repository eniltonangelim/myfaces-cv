from abc import ABCMeta, abstractmethod


class Recognizable (metaclass=ABCMeta):

    @abstractmethod
    def identify(self, embedder=None, image=None):
        raise NotImplementedError("recognizer model must define identify method")
