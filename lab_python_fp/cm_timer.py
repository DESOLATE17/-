from contextlib import contextmanager
import time

@contextmanager
def cm_timer_1():
    start_time = time.time()
    yield
    print("time: ",time.time()-start_time)

class cm_timer_2:
    def __init__(self):
        self.start_time = 0
    def __enter__(self):
        self.start_time = time.time()
    def __exit__(self, type, value, traceback):
        print("time: ", time.time() - self.start_time)

with cm_timer_1():
    time.sleep(5.5)

with cm_timer_2():
    time.sleep(5.5)


