import random

#a = int(input())

a = random.randint(1,9)
b = random.randint(1,9)
c = random.randint(1,9)
d = random.randint(1,9)

points = a*b*c*d
#points = random.randint(1,2000)
print("points = ",points)

 
if points<=100:
    b1 = (5)
    print("bonus = ",b1)

elif points>100:
    b1 = ((20/100)*points)
    print("bonus = ",round(b1,2))

elif points>1000:
    b1 = ((10/100)*points)
    print("bonus = ",round(b1,2))


if points%2 == 0:
    b2 = 1
    print("The number in even, so there is 1 additional point")
elif points%5 == 0:
    b2 = 2
    print("The number ends on a 5, so there are 2 additional points")
else:
    b2 = 0
    print('No additional bonuses')



if b2==1:
    print('maximum points:',round(points+b1+b2,0))
elif b2==2:
    print('maximum points:',round(points+b1+b2,0)) 
elif b2==0:
    print('maximum points: ',round(points+b1+b2,0))
