import configparser

class AppConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('conf.ini')