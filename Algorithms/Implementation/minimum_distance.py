n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

num = set([i for i in A if A.count(i) > 1])

occurs = list()
for j in num:
    occurs.append([i for i, x in enumerate(A) if x == j])

result = [abs(i[0] - i[1]) for i in occurs]
if result:
    print(min(result))
else:
    print(-1)
