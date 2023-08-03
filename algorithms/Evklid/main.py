def gcd(n1: int, n2: int) -> int:
    while n1 and n2:
        n1 = n1%n2
        n1, n2 = n2, n1
    return n1
