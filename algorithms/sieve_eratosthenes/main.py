def sieve_eratosthenes(n: int) -> list[int]:
    is_prime = [1] * (n + 1)

    for d in range(3, int(n**0.5)+1, 2):
        if is_prime[d]:
            for num in range(pow(d, 2), n+1, d*2):
                is_prime[num] = 0

    return [2] + [i for i in range(3, n+1, 2) if is_prime[i]]
