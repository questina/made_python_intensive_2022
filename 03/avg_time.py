import random
import time


def mean(k):
    def decorator(func):
        exec_time = []

        def cnt_calls(*args):
            start = time.time()
            func(*args)
            end = time.time()

            if len(exec_time) > k - 1:
                exec_time.pop(0)
            exec_time.append(end - start)
            print(sum(exec_time) / len(exec_time))

        return cnt_calls

    return decorator


@mean(10)
def some_func(a, b):
    sleep_time = random.randint(a, b)
    time.sleep(sleep_time)


for _ in range(10):
    some_func(1, 4)
