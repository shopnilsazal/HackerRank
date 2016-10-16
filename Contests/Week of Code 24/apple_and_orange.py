#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]


def get_fruit_count(fruit, pos, s, t):
    count = 0
    for f in fruit:
        f_pos = f + pos
        if f_pos in range(s, t+1):
            count += 1
    return count

apple_count = get_fruit_count(apple, a, s, t)
orange_count = get_fruit_count(orange, b, s, t)

print(apple_count)
print(orange_count)
