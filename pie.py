import matplotlib.pyplot as plt
import random
def f(n):
  ls=[i for i in range(0,1000)]
  values=random.choices(ls,k=n)
  plt.pie(values)
  plt.show()