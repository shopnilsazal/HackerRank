import itertools


def primes():
    yield 2
    yield 3
    yield 5
    yield 7
    ps = (p for p in primes())  # additional primes supply
    p = next(ps) and next(ps)  # discard 2, then get 3
    q = p * p  # 9 - square of next prime to be put
    sieve = {}  # into sieve dict
    n = 9  # the candidate number
    while True:
        if n not in sieve:  # is not a multiple of previously recorded primes
            if n < q:  # n is prime
                yield n
            else:
                add(sieve, q + 2 * p, 2 * p)  # n==p*p: for prime p, under p*p + 2*p,
                p = next(ps)  # add 2*p as incremental step
                q = p * p
        else:
            s = sieve.pop(n)
            add(sieve, n + s, s)
        n += 2  # work on odds only


def add(sieve, next, step):
    while next in sieve:  # ensure each entry is unique
        next += step
    sieve[next] = step  # next non-marked multiple of a prime


def primes_up_to(limit):
    return list(itertools.takewhile(lambda p: p <= limit, primes()))


def get_nth_prime(n):
    return next((pnum for index, pnum in enumerate(primes()) if index == n - 1))

t = int(input().strip())

for a in range(t):
    n = int(input().strip())
    print(get_nth_prime(n))
