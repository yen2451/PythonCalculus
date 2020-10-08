import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x**3+5*x
sequence=[1,2,3,4,5,6,7,8,9,10]
x = np.linspace(-10,10, num=100)
y = f(x)
plt.plot(x, y)
plt.show(
