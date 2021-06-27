import math

def euler(f,t0,x0,tEnd,n):
  h = (tEnd - t0) / n 
  x = t0 
  y = x0
  for i in range(n):
    y += h*f(x,y)
    x += h 
  return y 

import math
def f(t,x):
  y = -15 * x
  return y 

euler(f,0,1,1,8)