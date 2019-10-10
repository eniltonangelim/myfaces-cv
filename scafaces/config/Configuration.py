from scafaces.adapter.embeddable.OpenCVEmbedded import OpenCVEmbedded
from scafaces.adapter.detectable.OpenCVDetector import OpenCVDetector
from scafaces.adapter.dataset.DataSetImage import DataSetImage
from scafaces.adapter.trainable.SkLearnTrain import SkLearnTrain
from scafaces.adapter.recognizable.OpenCVRecognizer import OpenCVRecognizer

from scafaces.domain.ports.Configurable import Configurable
from scafaces.domain.ports.CreateUsecases import CreateUsecases
from scafaces.domain.ports.RecognizeUsecases import RecognizeUsecases

from scafaces.usecases.embeddable.FindEmbedder import FindEmbedder
from scafaces.usecases.detectable.FindDetector import FindDetector
from scafaces.usecases.dataset.FindImages import FindImages
from scafaces.usecases.embeddable.CreateEmbedder import CreateEmbedder
from scafaces.usecases.trainable.CreateTrainModel import CreateTrainModel
from scafaces.usecases.recognizable.RecognizeEmbedder import RecognizeEmbedder


class Configuration(Configurable):

    def getFindEmbedded(self):
        return FindEmbedder(OpenCVEmbedded())

    def getFindDetector(self):
        return FindDetector(OpenCVDetector())

    def getFindImages(self):
        return FindImages(DataSetImage())

    def getCreateEmbedded(self) -> CreateUsecases:
        return CreateEmbedder(OpenCVEmbedded())

    def getTrain(self) -> CreateUsecases:
        return CreateTrainModel(SkLearnTrain())

    def recognizeEmbedder(self) -> RecognizeUsecases:
        return RecognizeEmbedder(OpenCVRecognizer())

