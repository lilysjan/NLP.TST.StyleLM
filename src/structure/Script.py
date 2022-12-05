class Script(object):
    def __init__(self, raw):
        self.line = raw

        # Type은 크게
        # "line": 대사
        # "act": 인물명
        # "char": 행동지문
        self.type = None

    def __str__(self):
        return self.line[:5] if len(self.line) > 4 else self.line

    # TODO
    def check_type(self):
        if '(' in self.line:
            return 'act'
        else:
            return 'line'
