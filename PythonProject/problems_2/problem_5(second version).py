import random

a = random.randint(1,50)
b = random.randint(1,50)
c = random.randint(1,50)

total = a+b+c

timeInSeconds = total%60
timeInMinutes = int(total/60)

if timeInSeconds<10:
    print(f"{timeInMinutes}:0{timeInSeconds}")
else:
    print(f"{timeInMinutes}:{timeInSeconds}")
    