m = int(input('minutes ='))
h = int(input('hours ='))
a = h%24
b = m + 15
c = h + 1
d = c%24



if b > 59:
    b = b%60
elif h > 23:
    a = h%24
elif b > 59:
    c = (h + 1)
elif c > 23:
    d = c%24


print(f'{d}:{b}')