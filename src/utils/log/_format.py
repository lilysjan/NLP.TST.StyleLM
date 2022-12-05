def section_decorator(func):
    def wrapper():
        wid = 70
        print('-'*wid)
        func()
        print('-' * wid)
    return wrapper
