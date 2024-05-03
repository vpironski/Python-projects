import math as m
line = input()
line = line.split(",")
r1=int(line[0])/10
h1=int(line[1])/10
r2=int(line[2])/10
h2=int(line[3])/10
v1=r1**2*m.pi*h1
v2=r2**2*m.pi*h2
if (v1>v2):
    print("%.2f" % v1)
else:
    print("%.2f" % v2)