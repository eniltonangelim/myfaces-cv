from scafaces.domain.ports.DataSet import DataSet
from scafaces.domain.ports.FindUsecases import FindUsecases


class FindImages(FindUsecases):

    def __init__(self, repository: DataSet):
        self.__repository = repository

    def read(self):
        return self.__repository.getImages()