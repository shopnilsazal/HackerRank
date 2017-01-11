n, c, m = map(int, input().strip().split(' '))
p = list(map(int, input().strip().split(' ')))

if max(p) <= (c + m):
    print('Yes')
else:
    print('No')
