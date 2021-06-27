def Z(x,n):
  ret = 1
  nterm = 1

  for k in range(1,n+1):
    nterm = nterm * (-1) * (x**2)/k
    newret = ret + nterm
    if newret-ret==0:
      print("Terminated at n=",k)
      break
    ret=newret
  print(ret)

Z(10,1000000)

M= 3.89 #Use M=4!

def Z(n):
  ret=0
  for k in range(0,n+1):
    ret = ret + ((-1)**k)/(2*k+1)
  print(M*ret)

Z(10)