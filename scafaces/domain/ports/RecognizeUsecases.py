from abc import ABCMeta, abstractmethod


class RecognizeUsecases(metaclass=ABCMeta):

    @abstractmethod
    def identify(self, detector=None, embedder=None, recognizer=None, labelEncoder=None, image=None):
        raise NotImplementedError("recognizer model must define identify method")
