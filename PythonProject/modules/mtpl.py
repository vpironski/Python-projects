import matplotlib.pyplot as plt
import numpy as np

#a = int(input('a = '))
#b = int(input('b = '))
#c = int(input('c = '))
a = 1
b = 2
c = 3

x = np.arange(-10, 10, 0.1)
y = a*x**2+b*x+c

plt.plot(x,y)
plt.show()