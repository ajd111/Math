def FE(A,b):
  n = len(A)
  for k in range(0, n - 1):  #k represents the step of forward elimination you're currently doing
    for i in range(k + 1, n):  #i represents the range of rows under k
      #Calculate the multiplier.
      xMulti = A[i][k] / A[k][k]
      for j in range(k, n): #j represents the column in row j on which you're operating
        #Rewrite the entry $a_{ij}$ in the matrix $A$.
        A[i][j] = A[i][j] - ((xMulti) * (A[k][j]))
      #Rewrite the entry $b_i$ in the vector $b$.
      b[i] = b[i] - ((xMulti) * (b[k]))
  return A, b

A = [[1,2,1],[3,2,4],[4,4,3]]
b = [5,17,26]

print(FE(A,b))

def BS(A,b):
  n = len(A)
  x = [b[i] / A[i][i] for i in range(n)]
  for i in range(n - 2, -1, -1):
    sum = b[i] 
    for j in range(i + 1, n):
      sum = sum - ((A[i][j]) * (x[j]))
    x[i] = (sum / A[i][i])
  return x
A = [[1,2,1],[0,-4,1],[0,0,-2]]
b = [5,2,4]

print(BS(A,b))

def NGE(A,b):
  n = len(A)
  for k in range(0, n - 1):  #k represents the step of forward elimination you're currently doing
    for i in range(k + 1, n):  #i represents the range of rows under k
      #Calculate the multiplier.
      xMulti = A[i][k] / A[k][k]
      for j in range(k, n): #j represents the column in row j on which you're operating
        #Rewrite the entry $a_{ij}$ in the matrix $A$.
        A[i][j] = A[i][j] - ((xMulti) * (A[k][j]))
      #Rewrite the entry $b_i$ in the vector $b$.
      b[i] = b[i] - ((xMulti) * (b[k]))
  #return A, b

  n = len(A)
  x = [b[i] / A[i][i] for i in range(n)]
  for i in range(n - 2, -1, -1):
    sum = b[i] 
    for j in range(i + 1, n):
      sum = sum - ((A[i][j]) * (x[j]))
    x[i] = (sum / A[i][i])
  return x

#A=[[1,2,1],[3,2,4],[4,4,3]]
#b=[5,17,26]

#NGE(A,b)