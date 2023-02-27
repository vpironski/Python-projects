import random
from datetime import timedelta,datetime

a = random.randint(1,50)
b = random.randint(1,50)
c = random.randint(1,50)
d = a+b+c


print ('First racer:',str(timedelta(seconds = a)))
print ('Second racer:',str(timedelta(seconds = b)))
print ('Third racer:', str(timedelta(seconds = c)))
print ('Total time:',str(timedelta(seconds = d)))