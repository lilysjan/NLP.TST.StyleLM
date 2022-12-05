

class Movie(object):
    def __init__(self, fname, raw):
        self.raw = raw
        self.fname = fname
        self.characters = list()

        self.scripts = list()
        self.preprocess()

    def preprocess(self):
        self.scripts = []

