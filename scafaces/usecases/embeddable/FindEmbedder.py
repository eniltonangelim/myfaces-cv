from scafaces.domain.ports.Embeddable import Embeddable
from scafaces.domain.ports.FindUsecases import FindUsecases


class FindEmbedder(FindUsecases):

    def __init__(self, embeddable: Embeddable):
        self.__embeddable = embeddable

    def read(self):
        return self.__embeddable.read()
