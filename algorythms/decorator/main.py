from time import perf_counter_ns


def time(fn):

    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        fn(*args, **kwargs)
        end = perf_counter_ns()
        print('[INFO] function "{0}" ran in {1} seconds'.format(
            fn.__name__,
            (end-start) / pow(10, 9)
        ))
        return fn(*args, **kwargs)

    return wrapper