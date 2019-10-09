from scafaces.domain.ports.Configurable import Configurable

class Application():

    def __init__(self, config: Configurable):
        self.__usecases = config

    def run(self):

        self.__usecases.getCreateEmbedded().create(self.__usecases.getFindDetector().extract(
            self.__usecases.getFindImages().read(),
            self.__usecases.getFindEmbedded().read()
        ))

        self.__usecases.getTrain().recognizer()



if __name__ == '__main__':
    from scafaces.config.Configuration import Configuration

    app = Application(Configuration())
    app.run()
