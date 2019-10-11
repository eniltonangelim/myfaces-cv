import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from os import environ
from typing import NoReturn
from scafaces.domain.ports.Trainable import Trainable


class SkLearnTrain(Trainable):

    def __init__(self):
        self.__embeddings = environ.get("EMBEDDING_OUTPUT")
        self.__recognizer = environ.get("RECOGNIZER_OUTPUT")
        self.__labelEncoder = environ.get("LABEL_OUTPUT")
        self.__le = LabelEncoder()

    def recognizer(self) -> NoReturn:
        data = pickle.loads(open(self.__embeddings, "rb").read())

        labels = self.__le.fit_transform(data["names"])
        recognizer = SVC(C=1.0, kernel="linear", probability=True)
        recognizer.fit(data["embeddings"], labels)

        self.save(self.__recognizer, recognizer)
        self.save(self.__labelEncoder, self.__le)


    def save(self, file, data) -> NoReturn:

        rec = open(file, "wb")
        rec.write(pickle.dumps(data))
        rec.close()
