import asyncio

from functools import wraps
from time import perf_counter


def timer(func):
    start = None
    end = None

    @wraps(func)
    async def wrapper(*args, **kwargs):
        nonlocal start
        nonlocal end
        start = perf_counter()
        try:
            result = await func(*args, **kwargs)
        finally:
            end = perf_counter()
            print(f"Function {func.__name__} took {end - start} s")
        return result
    return wrapper
