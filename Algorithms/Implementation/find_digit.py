
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nums = map(int, list(str(n)))
    count = 0
    for i in nums:
        if i != 0:
            if n % i == 0:
                count += 1
    print(count)

