n = int(input())
d = 10
total = sum(pow(i, i, 10**d) for i in range(1, n+1))
result = int(str(total)[-10:])
print(result)
