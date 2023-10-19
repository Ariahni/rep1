import matplotlib.pyplot as plt
from math import cos, sin
import numpy as np

x = np.linspace(0.1,10,50)
y1 = [cos(i) for i in x]
y2 = [sin(i) for i in x]
y3 = [i ** 2 for i in x]
y4 = [2 / i for i in x]
plt.figure(figsize=(5, 7))
plt.subplot(4, 1, 1)
plt.plot(x, y1, "r")
plt.title("Зависимости y1= cos(x), y2 = sin(x), y3 = x^2, y4 = 2/x")
plt.ylabel("y1", fontsize=12)
plt.grid(True)
plt.subplot(4, 1, 2)
plt.plot(x, y2, "r")
plt.ylabel("y2", fontsize=12)
plt.grid(True)
plt.subplot(4, 1, 3)
plt.plot(x, y3, "r")
plt.ylabel("y3", fontsize=12)
plt.grid(True)
plt.subplot(4, 1, 4)
plt.plot(x, y4, "r")
plt.ylabel("y4", fontsize=12)
plt.xlabel("x", fontsize=12)
plt.grid(True)
plt.show()