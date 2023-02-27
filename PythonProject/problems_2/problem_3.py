
import random


a = random.randint(1,100)
b = random.randint(1,100)

print("a = ",a)
print("b = ",b)

if a%2 == 0:
    print('a = even')
else:
    print('a isnt even') 


if a>b:
    print('a is the bigger number')
elif b>a:
    print('b is the bigger number')
else: 
    print('a is equal to b')