from typing import (
    Callable,
    Any,
)


def repeat(n: int) -> Any:
    def wrapper(func: Callable) -> Any:
        def inner_wrapper(*args, **kwargs) -> Any:
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return inner_wrapper
    return wrapper


@repeat(
    n=5
)
def main():
    print(5)
    return 10


print(main())