def my_dec(a, b):
    def dec(fn):
        from functools import wraps
        
        @wraps(fn)
        def inner(*args, **kwargs):
            print("Decorated function called: a={0}, b={1}".format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec