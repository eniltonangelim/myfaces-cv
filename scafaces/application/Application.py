from scafaces.domain.ports.Configurable import Configurable


class Application():

    def __init__(self, config: Configurable):
        self.__usecases = config

    def run(self):
        images = self.__usecases.getFindImages().read()
        embedder =  self.__usecases.getFindEmbedded().read()

        model = self.__usecases.getFindDetector().extract(images, embedder)

        self.__usecases.getCreateEmbedded().create(model)
        self.__usecases.getTrain().recognizer()
        self.__usecases.recognizeEmbedder().identify(embedder, "/home/angelim/Downloads/DSC_0043.JPG")


if __name__ == '__main__':
    from scafaces.config.Configuration import Configuration

    app = Application(Configuration())
    app.run()
