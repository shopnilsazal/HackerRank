from math import sqrt
t = int(input())
count = 1
while count <= t:
    tn = int(input())
    result = 0
    n = int((-1 + sqrt(1+8*tn)) / 2)
    if (n * (n+1) / 2) == tn:
        result = n
    else:
        result = -1

    print(result)
    count += 1
