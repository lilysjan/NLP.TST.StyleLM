import copy
from src.structure.Script import Script


class Movie(object):
    def __init__(self, fname, raw):
        if type(raw) == list:
            raw = ''.join(raw)
        self.raw = raw
        self.fname = fname
        self.file_qual = None
        self.prep_type = None
        self.prep_qual = None

        self.scripts = list()
        self.characters = list()
        self.preprocess()

    def preprocess(self):
        # 사전검사들
        self.file_qual = check_file_quality(self.raw)
        self.prep_type = check_prep_type(self.raw)
        self.prep_qual = check_prep_quality(self.raw)

        self.raw = self.makeup_raw()
        # 전처리의 성능을 보기 위해선 script에 결과를 저장해야하는 것들
        self.scripts = [Script(i) for i in self.raw]

    # TODO: 스크립트 유형 처리에 맞게 나눠야 함. 일단은 임의로 나눈 상태
    def makeup_raw(self):
        res = self.raw.split('\n\n')
        return res


# TODO
def check_file_quality(raw):
    return 1


# TODO
def check_prep_type(raw):
    return 1


# TODO
def check_prep_quality(raw):
    return 1
