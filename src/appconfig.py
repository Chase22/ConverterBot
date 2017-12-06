import configparser, os

class AppConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'config', 'conf.ini')
        print(path)
        self.config.read(path)
        print(self.config.sections())