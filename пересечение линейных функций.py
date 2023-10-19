import matplotlib.pyplot as plt
import numpy as np
def f(f1,f2):
  x = np.linspace(-10, 10, 100)
  y1 = eval(f1)
  y2 = eval(f2)
  plt.plot(x, y1, label='f1')
  plt.plot(x, y2, label='f2')
  plt.grid(True)
  plt.show()