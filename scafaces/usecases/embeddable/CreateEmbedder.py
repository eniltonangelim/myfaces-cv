from scafaces.domain.ports.Embeddable import Embeddable
from scafaces.domain.ports.CreateUsecases import CreateUsecases
from scafaces.domain.models.People import People

class CreateEmbedder(CreateUsecases):

    def __init__(self, embeddable: Embeddable):
        self.__embeddable = embeddable

    def create(self, data: People):
        self.__embeddable.create(data)

    def recognizer(self):
        pass

