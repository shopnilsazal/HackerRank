t = int(input().strip())

for a in range(t):
    chars = input().strip()
    list_chars = list(chars)
    count = 0
    for l in range(1, len(list_chars)):
        if list_chars[l-1] == list_chars[l]:
            count += 1

    print(count)
