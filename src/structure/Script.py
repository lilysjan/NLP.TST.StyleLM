import re


class Script(object):
    def __init__(self, raw, stype=None):
        self.line = raw

        # Type은 크게
        # "line": 대사
        # "act": 행동지문
        # "char": 인물명
        self.stype = stype if stype is not None else self.check_type(raw)

    def __str__(self):
        return self.line[:5] if len(self.line) > 4 else self.line

    @staticmethod
    def check_type(raw):
        p = re.compile(r'[\?\[\<\(|||:/#\)]+')
        # if r'[\(\<\[]' in raw:
        if p.match(raw) is not None:
            return 'act'
        else:
            return 'line'
