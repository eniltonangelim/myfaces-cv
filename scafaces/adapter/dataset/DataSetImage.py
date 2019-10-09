from os import environ
from typing import List
from imutils import paths

from scafaces.domain.ports.DataSet import DataSet


class DataSetImage(DataSet):

    def __init__(self):
        self.__name = environ.get("DATASET_NAME")
        self.__path = environ.get("DATASET_PATH")

    def get_name(self):
        return self.__name

    def get_path(self):
        return self.__path

    def getImages(self) -> List[str]:
        return list(paths.list_images(self.get_path()))