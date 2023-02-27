import math
import cmath


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c= '))

text = '{0} + {1} = {2}'   #method 1
print(text.format(a,b,a+b))

print(str(a)+' + '+str(b)+' = ' +str(a+b))   #method 2

#method 1 = method 2

#rounding up
print(math.ceil(34.25))
print(math.floor(34.25))
print(round(23.54,1))


d = b**2 - 4*a*c

if d == 0:
    x = -b/(2*a)
    print('x= ', x)
else:
    x1 = (-b-cmath.sqrt(d))/(2*a)
    x2 = (-b+cmath.sqrt(d))/(2*a)
    print('x1= ' + str(x1), 'x2= '+str(x2), sep='\n')