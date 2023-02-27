
m = int(input('minute -> '))
h = int(input('hours -> '))

minutes = (m + 15)%60
hours = int(h+((m + 15)//60))

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')

