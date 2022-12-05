import datetime


def section_decorator(func):
    def wrapper(*args, **kwargs):
        wid = 70
        print('-'*wid)
        func(*args, **kwargs)
        print('-' * wid)
    return wrapper


def get_today():
    return datetime.datetime.today().strftime('%Y-%m-%d')
