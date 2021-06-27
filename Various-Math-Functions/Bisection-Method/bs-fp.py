def bisection(f,a,b,nmax,eps):
  fa = f(a)
  fb = f(b)
  if fa*fb>=0:
    print('The function has the same sign at each endpoint of [a,b] and may not have a root.  Code terminated')
    return
  error = b-a
  for n in range(0,nmax+1):
    error = error/2
    c = a+error
    fc = f(c)
    if error < eps:
      print('The method has converged to the desired accuracy.  The root is ' + str(c) +'.')
      return
    if fa * fc < 0:
      b = c
      fb = fc
    else:
      a = c
      fa = fc
  print('After ' + str(nmax) +' iterations, the bisection method returned a root of ' + str(c) + '.')

def f(x):
  y = x**2+3*x+2
  return y

a=-10
b=-1.5
bisection(f,a,b,100,10**-10)

def falseposition(f,a,b,nmax):
  fa = f(a)
  fb = f(b)
  if fa*fb>=0:
    print('The function has the same sign at each endpoint of [a,b] and may not have a root.  Code terminated')
    return
  #error = b-a
  for n in range(0,nmax+1):
    #error = error/2
    c = (a*fb - b*fa / (fb-fa))
    fc = f(c)
    #if error < eps:
      #print('The method has converged to the desired accuracy.  The root is ' + str(c) +'.')
      #return
    if fa * fc < 0:
      b = c
      fb = fc
    else:
      a = c
      fa = fc
  print('After ' + str(nmax) +' iterations, the false position method returned a root of ' + str(c) + '.')

def f(x):
  y = x**2+3*x+2
  return y

a=-10
b=-1.5
falseposition(f,a,b,100)