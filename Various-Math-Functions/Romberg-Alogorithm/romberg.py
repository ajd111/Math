import math

def f(x):
  y= i * Math.sin(x) 
  return y

def Romberg(n):
  a = 0
  b = 1

  r = []
  h = (b - a)
  r.append([(h / 2.0)*(f(a) + f(b))])
  for i in range(1, n + 1):
    h = (h/2)
    sum = 0
    for k in range(1, 2**i, 2):
      sum = sum + f(a + k * h)
    rowi = [(1/2) * r[i - 1][0]  + sum * h]
    for j in range(1, i + 1):
      rij = rowi[j - 1] + (rowi[j - 1] - r[i - 1][j - 1]) / (4**j-1)
      rowi.append(rij)
    r.append(rowi)
  print(*r, sep='\n')


Romberg(10)

