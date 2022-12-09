import copy
from src.structure.Script import Script
import numpy as np


class Movie(object):
    def __init__(self, meta, raw):
        if type(raw) == list:
            raw = ''.join(raw)
        self.raw = raw
        self.fname = meta['원본파일명']
        self.name = meta['영화명']
        self.genre = meta['장르']
        # NOTE: 가끔 '할'처럼 이름과 단어가 구분이 안될 수도 있다.
        self.characters = enum_characters(meta['배역'])

        self.file_qual = None
        self.prep_type = None
        self.prep_qual = None

        self.scripts = list()
        self.preprocess()

    def preprocess(self):
        # 사전검사들
        self.file_qual = check_file_quality(self.raw)
        self.prep_type = check_prep_type(self.raw)
        self.prep_qual = check_prep_quality(self.raw)

        # 전처리의 성능을 보기 위해선 script에 결과를 저장해야하는 것들
        self.scripts = self.makeup_script()

    # TODO: 스크립트 유형 처리에 맞게 나눠야 함. 일단은 임의로 나눈 상태
    def makeup_script(self):
        chunk = self.raw.split('\n\n')
        if len(self.characters) == 0 or self.characters is None:
            return chunk
        else:
            tick = dict()
            res = []
            for char in self.characters:
                tick[char] = list(map(lambda x: char in x[:len(char)], chunk))
            chars = list(tick.keys())

            for i, case in enumerate(zip(*list(tick.values()))):
                if sum(case) != 0:
                    idx = [j for j, char in enumerate(tick.keys()) if case[j]][0]
                    res.append(Script(chars[idx], stype='char'))
                res.append(Script(chunk[i]))
            return res

    def get_act_num(self):
        return len([i for i in self.scripts if i.stype=='act'])

    def get_line_num(self):
        return len([i for i in self.scripts if i.stype=='line'])

    def get_char_num(self):
        return len([i for i in self.scripts if i.stype=='char'])

    def get_lines(self):
        return [i.line for i in self.scripts if i.stype == 'line']


# TODO
def check_file_quality(raw):
    return 1


# TODO
def check_prep_type(raw):
    return 1


# TODO
def check_prep_quality(raw):
    return 1


def enum_characters(dat):
    res = copy.deepcopy(dat)
    for character in dat:
        if len(character) == 3:
            res.append(character[1:])
    return res
