import math

figure = str(input('figure -> '))

if figure == 'square':
    a = float(input('a = '))
    print('P =',round(4*a,3))
    print('S =',round(a*a,3))

elif figure == 'rectangle':
    a = float(input('a = '))
    b = float(input('b = '))
    print('P =',round(a+a+b+b,3))
    print('S =',round(a*b,3))

elif figure == 'circle':
    r = float(input('r = '))
    print('C =',round(2*r*math.pi,3))
    print('S =', round(math.pi*r**2,3))

elif figure == 'triangle':
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    h = float(input('h = '))
    print('P = ',round(a+b+c,3))
    print('S = ',round((a*h)/2,3))

else:
    print('I do not know this figure')

    
    