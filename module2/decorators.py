from functools import wraps


def get_args_string(args, kwargs) -> str:
    args_ = [str(a) for a in args]
    kwargs_ = ["{0}={1}".format(k, v) for (k, v) in kwargs.items()]
    all_args = args_ + kwargs_
    args_str = ",".join(all_args)
    return args_str


# Decorator function
def counter(fn):
    cnt = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print("{0} was called {1} times".format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

# Sparametryzowany dekorator składa się z: dekoratora zewnętrznego z argumentem (timed(n)), dekoratora właściwego przyjmującego funkcję do dekoracji (inner_decorator(fn)),
# a także funkcji wrapującej (inner(*args, **kwargs)).
def timed(n: int = 1) -> float:
    """Get average execution time of passed function through n executions"""
    def inner_decorator(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            elapsed_total = 0

            for _ in range(n):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                elapsed_total += end - start

            args_str = get_args_string(args, kwargs)

            print("{0}({1}) took {2:.6f}s to run through {3} executions.".format(
                fn.__name__, args_str, elapsed_total / n, n))

            return result
        return inner
    return inner_decorator


class DecoratorClass:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __call__(self, fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            print("Decorated function called: a={0}, b={1}".format(
                self.a, self.b))
            return fn(*args, **kwargs)
        return inner


def log(fn):
    from datetime import datetime

    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        args_str = get_args_string(args[1:], kwargs)

        print("{0}: Executed {1}({2}).".format(datetime.now(), fn.__name__, args_str))
        return result
    return inner


def log_all(cls):
    import inspect

    methods = inspect.getmembers(cls, inspect.isfunction)

    for method_name, method_instance in methods:
        if "__" not in method_name:
            setattr(cls, method_name, log(method_instance))

    return cls
