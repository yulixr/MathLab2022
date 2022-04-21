import math
import matplotlib.pyplot as plt
import numpy as np

def F(x):
    return 4**x
def Quads(func, n, metod, a, b):
  summ = 0
  y = []
  h = (b - a) / n
  start = a + metod * h
  for i in range(n):
    summ += func(start + i * h)
    y.append(func(start+i * h))
  return summ * h, y

def Integral(func, n, metod, a, b):
  if metod == 0:
    res, y = Quads(func, n, 0.0, a, b)
    x = np.linspace(a, b, n)
    plt.bar(x, y, width=1/n,edgecolor="k", align = "edge")
    return res
  elif metod == 1:
    res, y = Quads(func, n, 1.0, a, b)
    x = np.linspace(a, b, n)
    plt.bar(x, y, width=-1/n,edgecolor="k", align = "edge")
    return res
  elif metod == 2:
    res, y = Quads(func, n, 0.5, a, b)
    x = np.linspace(a, b, n)
    plt.bar(x, y, width=1/n,edgecolor="k")
    return res

print("Input a b:")
a, b = map(int, input().split())
print("Input n - number of sht")
n = int(input())
print("Input metod:\n\t 0 - left rectangles\n\t 1 - right rectangles\n\t 2 - middle rectangles")
metod = int(input())
x = np.linspace(a, b, n)
y_ideal = [F(a) for a in x]
plt.plot(x, y_ideal, color = "orange")
res = Integral(F, n, metod, a, b)
plt.grid()
plt.title("Integral " + str(round(res, 2)) + " with metod " + ("left rectangles" if(metod == 0) else("right rectangles" if (metod == 1) else "middle rectangles")))
plt.show()
