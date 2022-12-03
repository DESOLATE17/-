def prime_generator(n):
    sieve = set(range(2, n+1))
    while sieve:
        prime = min(sieve)
        yield prime
        sieve -= set(range(prime, n+1, prime))
