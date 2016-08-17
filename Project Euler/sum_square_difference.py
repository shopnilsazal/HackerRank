t = int(input().strip())

for a in range(t):
    n = int(input().strip())
    n_sum_square = (n * (n+1) / 2) ** 2
    n_square_sum = (n * (n+1) * ((2*n) + 1)) / 6
    print(int(abs(n_sum_square - n_square_sum)))
