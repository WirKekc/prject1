from time import time


# Реализовать декоратор, который измеряет скорость выполнения функций
def timer(func):
    def measure_time(*args, **kwargs):
        start = time()
        end_func = func(*args, **kwargs)
        end = time()
        print('{} is working for {} seconds'.format(func.__name__, (end - start)))
        return end_func
    return measure_time


@timer
def func123():
    a = 0
    for i in range(0, 150):
        a += i
    return a


func123()
