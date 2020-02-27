from contextlib import contextmanager
from time import time, sleep


@contextmanager
def locker(somelock):
    somelock.lock = True
    yield somelock


class Lock(object):
    def __init__(self):
        self.lock = False


lock1 = Lock()
with locker(lock1):
    print('{} locked is {} '.format(lock1, lock1.lock))
# ------------------------------------------------

@contextmanager
def no_exceptions():
    try:
        yield
    except Exception as e:
        print('logs:' + str(e))

with no_exceptions():
    1/0

# --------------------------------------------------

class TimeIt(object):
    def __enter__(self):
        self.start_time = time()

    def __exit__(self, *args):
        self.stop_time = time()
        self.result = self.stop_time - self.start_time

timer = TimeIt()
with timer:
    sleep(3)

print('Execution time was:', timer.result)
