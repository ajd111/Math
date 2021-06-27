import math 

def bisect(a,b,nmax,eps):

  fa = f(a) 
  fb = f(b)
  if fa * fb >= 0:
    print("There is no sign change on the interval")
    return
  error = b - a 
  for i in range (1, nmax+1):
    error = error / 2
    m = a + error 
    fm = f(m)
    if abs(error) < eps:
      print("The root is", m, "and it took", i, "steps")
    if a * b >= 0 and a * m >= 0:
      a = m
      fa = fm
    else:
      b = m
      fb = fm

def f(x):
  #return x**3 * math.cos(x)
  #return math.exp(-0.01*x) * math.sin(0.2*x)
  #return x**10 - 8*x**3 + 2 * x - 0.25
  return x**2+3*x+2

bisect(1,2,50,10**-10)