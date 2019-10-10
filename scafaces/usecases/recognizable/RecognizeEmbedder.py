from scafaces.domain.ports.Recognizable import Recognizable
from scafaces.domain.ports.RecognizeUsecases import RecognizeUsecases


class RecognizeEmbedder(RecognizeUsecases):

    def __init__(self, recognize: Recognizable):
        self.__recognize = recognize

    def identify(self, embedder=None, image=None):
        self.__recognize.identify(embedder, image)