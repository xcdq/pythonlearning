import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorator
def f1():
    print('hello')


def f2():
    print('world')


def timee(funnn):
    print(time.time())
    funnn()


f1()
# timee(f1)
# timee(f2)
