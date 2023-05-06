from typing import (
    Callable,
    Any,
)


def repeat(n: int) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs) -> Any:
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return inner_wrapper
    return wrapper
