from detector_factory import DetectorFactory
from os import path

PROFILES_DIRECTORY = path.join(path.dirname(__file__), 'profiles')


class Predict(object):
    def __init__(self):
        self.factory =  DetectorFactory()
        self.factory.load_profile(PROFILES_DIRECTORY)
        self.detector = self.factory.create()

    def get_lang(self, text):
        self.detector.append(text)
        return self.detector.detect()