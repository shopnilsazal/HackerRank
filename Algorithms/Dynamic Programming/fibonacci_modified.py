def m_fib(t0, t1, n):
    for _ in range(3, n+1):
        t2 = t0 + t1 ** 2
        t0, t1 = t1, t2
    return t2

a, b, n = map(int, input().split())

print(m_fib(a, b, n))
