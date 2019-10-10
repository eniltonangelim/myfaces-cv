from scafaces.domain.ports.Detectable import Detectable
from scafaces.domain.ports.FindUsecases import FindUsecases
from scafaces.domain.models.People import People
from typing import List


class FindDetector(FindUsecases):

    def __init__(self, detectable: Detectable):
        self.__detectable = detectable

    def read(self):
        return self.__detectable.read()

    def extract(self, images: List[str], embedder = None) -> People:
        return self.__detectable.detector(images, embedder)