from functools import wraps
from time import perf_counter


def timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = perf_counter()
        result = await func(*args, **kwargs)
        end = perf_counter()
        print(f"Function {func.__name__} took {end - start} ms")
        return result
    return wrapper
