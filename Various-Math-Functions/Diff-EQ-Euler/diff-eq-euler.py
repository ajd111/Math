def step_test(a,b,n):
  a 
  b
  n
  h = (b-a)/n
  t1 = a
  for k in range(1, n):
    t1 = t1 + h
    t2 = a + k * h
  print(k)
  print(t1)
  print(t2)

step_test(0,1,100000)


def Euler(a,b,x,n):
  a 
  b 
  x
  n
  h = (b-a)/n
  t = a 
  for k in range(1, n+1):
    x = x + h * f(t,x)
    t = a + k * h  
  print(x)
  print(t)
  
def f(t,x):
  # RHS of diff. eq. being solved
    return t + x**2 

Euler(0,0.9,1,1000)



def num_6(a,b,x,n):
  a 
  b 
  x
  n
  h = (b-a)/n
  t = a 
  for k in range(1, n+1):
    xp = f(t,x)
    xpp = 1 + 2 * x * xp
    #xppp = 0 + 2 * x * xpp + xp * 2 * xp
    x = x + h * xp + (h**2/2) * xpp + (h**3/6) * xpp
    t = a + k * h  
  print(x)
  print(t)
  

def num_6_f(t,x):
  # RHS of diff. eq. being solved
    return t + x**2 

num_6(0,0.9,1,10000)