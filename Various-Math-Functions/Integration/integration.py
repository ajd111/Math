import math 

def left(a,b,n):
  h = (b-a) / n
  int = 0.0
  for i in range(0, n):
    int = int + f(a + i * h) 
  print(h * int)

def right(a,b,n):
  h= (b-a) / n
  int = 0.0
  for i in range(1, n+1):
    int = int + f(a + i * h)
  print(h * int)

def trap(a,b,n):
  h = (b-a)/n 
  trap = (f(a) + f(b)) / 2.0
  for i in range(1, n-1):
    trap = trap + f(a + i * h)
  print(h * trap)

def f(x):
  #return 3 * x + 10
  #return math.exp(-3 * x * x)
  return math.sin(x) / x

left(0,10,1000) 
right(0,10,1000)
trap(0,10,1000)