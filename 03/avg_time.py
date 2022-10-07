import time


def mean(k: int):
    """
    Decorator that measures average function execution time from last k calls
    :param k: number of last calls to measure average time execution
    """
    def decorator(func):
        exec_time = []

        def cnt_calls(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time()

            if len(exec_time) > k - 1:
                exec_time.pop(0)
            exec_time.append(end - start)
            print(sum(exec_time) / len(exec_time))

            return res

        return cnt_calls

    return decorator
