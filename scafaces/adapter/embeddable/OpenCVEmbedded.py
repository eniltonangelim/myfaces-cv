from scafaces.domain.ports.Embeddable import Embeddable
from scafaces.domain.models.People import People
from os import path, environ
import cv2
import pickle


class OpenCVEmbedded(Embeddable):

    def __init__(self):
        super()
        self.__modelPath = environ.get("EMBEDDING_MODEL")
        self.__embeddingOutput = environ.get("EMBEDDING_OUTPUT")

    def read(self):
        return cv2.dnn.readNetFromTorch(self.__modelPath)

    def create(self, people: People):
        data = {"embeddings": people.embeddings, "names": people.names}

        file = open(self.__embeddingOutput, "wb")
        pickle.dump(data, file)
        file.close()