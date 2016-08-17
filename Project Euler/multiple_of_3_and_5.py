t = int(input())


def multiple_sum(n):
    n1 = ((n / 3) - 1) if n % 3 == 0 else (n / 3)
    n2 = ((n / 5) - 1) if n % 5 == 0 else (n / 5)
    n3 = ((n / 15) - 1) if n % 15 == 0 else (n / 15)

    s1 = (3 * n1 * (n1 + 1)) / 2
    s2 = (5 * n2 * (n2 + 1)) / 2
    s3 = (15 * n3 * (n3 + 1)) / 2

    return (s1 + s2) - s3


count = 1
while count <= t:
    n = int(input())
    result = multiple_sum(n)
    print(result)
    count += 1

