n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
m = min(arr)


def arr_process(arr, m):
    temp_arr = []
    for i in arr:
        i -= m
        if i > 0:
            temp_arr.append(i)
    return len(temp_arr), temp_arr, min(temp_arr)

print(n)
while len(arr) > 1:
    n, arr, m = arr_process(arr, m)
    print(n)

