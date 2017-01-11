
def check_condition(n):
    count = 0
    for a in range(1, n+1):
        if (a ^ n > n) and (0 < a < n):
            count += 1
    return count

q = int(input().strip())
for _ in range(q):
    x = int(input().strip())
    # your code goes here
    print(check_condition(x))
