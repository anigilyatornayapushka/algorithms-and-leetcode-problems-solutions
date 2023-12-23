import math


def sundaram_sieve(n: int) -> list[int]:
    k = (n - 2) // 2
    is_prime = [True] * (k + 1)
    sqrt_k = math.isqrt(k)

    for i in range(1, sqrt_k + 1):
        if is_prime[i]:
            start = 2 * i * (i + 1)
            step = (i << 1) + 1
            max_range = (k - start) // step + 1
            is_prime[start : start + max_range * step : step] = [False] * max_range

    primes = [2] + [2 * i + 1 for i in range(1, k + 1) if is_prime[i]]

    return primes
