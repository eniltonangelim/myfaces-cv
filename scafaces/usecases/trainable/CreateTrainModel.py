from scafaces.domain.models.People import People
from scafaces.domain.ports.CreateUsecases import CreateUsecases
from scafaces.domain.ports.Trainable import Trainable

class CreateTrainModel(CreateUsecases):

    def __init__(self, train: Trainable):
        self.__train = train

    def create(self, data: People):
        pass

    def recognizer(self):
        self.__train.recognizer()

