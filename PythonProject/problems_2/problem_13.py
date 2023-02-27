

x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
x = int(input('x = '))
y = int(input('y = '))

 
if x > x1 and x < x2 and y < y1 and y > y2:
    print('The points are in the border')

else:
    print('The points are outside the border')