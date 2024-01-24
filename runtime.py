import time


def runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(round(time.time() - start, 5))
        return result

    return wrapper
