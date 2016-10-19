n = int(input())

numbers = [int(x) for i in range(n) for x in input().split()]
num_sum = str(sum(numbers))
print(num_sum[0:10])
