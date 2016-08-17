t = input()
time = t[0:-2]
ap = t[-2:]

new_time = time.split(':')
if ap == 'PM':
    hour = int(new_time[0])
    if 1 <= hour < 12:
        new_time[0] = str(hour + 12)
    print(':'.join(new_time))

if ap == 'AM':
    if int(new_time[0]) == 12:
        new_time[0] = '00'
    print(':'.join(new_time))

