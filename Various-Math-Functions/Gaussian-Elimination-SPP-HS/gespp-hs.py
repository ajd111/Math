import numpy as np
from scipy.linalg import hilbert


def NGE(A,b):
  n=len(A) # number of rows of A
  m=len(A[1]) # number of cols of A
  for i in range(n-1):
    for k in range(i+1,n):
      xmult = A[k][i]/A[i][i]
      for j in range(i+1,m):
        A[k][j]=A[k][j]-(xmult)*A[i][j]
      b[k]=b[k]-(xmult)*b[i]
  b[n-1]=b[n-1]/A[n-1][n-1]
  for i in range(n-2,-1,-1):
    sum = b[i]
    for j in range(i+1,n):
      sum=sum-A[i][j]*b[j]
    b[i]=sum/A[i][i]
  print(b)

A=[[1,3,-4],[2,-7,2],[1,-2,4]]
b=[0,-3,3]

#NGE(A,b)

def GESPP(A,b):
  n=len(A) # number of rows of A
  m=len(A[1]) # number of cols of A
  l=[0]*n
  s=[0]*n
###### Block 1 #####
  for i in range(n):  
    l[i]=i
    smax = 0
    for j in range(n):
      smax=max([smax, abs(A[i][j])])
    s[i]=smax
###### Block 2 #####  
  for k in range(n-1):
    rmax=0
    for i in range(k,n):
      r = abs(A[l[i]][k]/s[l[i]])
      if r>rmax:
        rmax=r
        j=i
    l[k],l[j]=l[j],l[k]
    for i in range(k+1,n):
      xmult = A[l[i]][k]/A[l[k]][k]
      #A[l[i]][k]=xmult
      for j in range(k+1,n):
        A[l[i]][j]=A[l[i]][j]-(xmult)*A[l[k]][j]
      b[l[i]]=b[l[i]]-(xmult)* b[l[k]]
###### Block 3 #####
  b[l[n-1]]=b[l[n-1]]/A[l[n-1]][n-1]
  for i in range(n-2,-1,-1):
    sum=b[l[i]]
    for j in range (i+1,n):
      sum=sum-A[l[i]][j]*b[l[j]]
    b[l[i]]=sum/A[l[i]][i]
###### Block 4 #####
  x=[0]*n
  for i in range(n):
    x[i]=b[l[i]]

  print(x)

A=[[1,3,-4],[2,-7,2],[1,-2,4]]
b=[0,-3,3]

#GESPP(A,b)

H=hilbert(100) #This creates a special matrix called the Hilbert matrix of size 100x100.
vector3=H.dot(np.ones(100))
#NGE(H,vector3)

H=hilbert(100) #This creates a special matrix called the Hilbert matrix of size 100x100.
vector3=H.dot(np.ones(100))
#GESPP(H,vector3)