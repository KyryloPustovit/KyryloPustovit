from numpy import *
import matplotlib.pyplot as plt

x=linspace(-4,4,51) 
y=5*sin(1/x)*cos(x**2)**3

plt.plot(x, y)
plt.show()
