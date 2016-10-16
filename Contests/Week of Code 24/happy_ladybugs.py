from collections import Counter

t = int(input().strip())

def traverse_string(s):
    count = 0
    for c1, c2 in zip(s, s[1:]):
        if c1 == c2:
            count += 1
    if count == len(set(s)):
        return True
    return False

for _ in range(t):
    n = int(input().strip())
    b = input().strip()
    freq = dict(Counter(b))
    if n == 0:
        print('NO')
    elif n == 1 and b != '_':
        print('NO')
    elif b.count('_') == n:
        print('YES')
    elif '_' in b:
        del(freq['_'])
        if min(freq.values()) == 1:
            print('NO')
        else:
            print('YES')
    elif n > 1 and b == n * b[0]:
        print('YES')
    elif traverse_string(b):
        print('YES')
    else:
        print('NO')

