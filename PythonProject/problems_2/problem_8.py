speed = float(input('speed = '))

if speed <= 10:
    print('speed -> slow')
elif speed>10 and speed <= 50:
    print('speed -> avarage')
elif speed > 50 and speed <= 150:
    print('speed -> fast')
elif speed > 150 and speed <= 1000:
    print('speed -> ultra fast')
else:
    print('speed -> extremely fast')
