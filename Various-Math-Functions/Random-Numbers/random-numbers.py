import random 
import random as rn
import matplotlib.pyplot as plt
import math

############################
## 1-a MERSENNE GENERATOR ##
############################

def test_m_random(s,n):
# Generates n random numbers in [0,5)
# using the Mersenne generator and 
# checks for uniform distribution
  x = [0 for i in range(10)]
  k = 16807
  j = 2147483647
  for i in range(n):
    s = (k * s) % j
    r = s / j
    num = 5 * r
    if num < 0.5:
      x[0] = x[0] + 1
    elif num < 1.0:
      x[1] = x[1] + 1
    elif num < 1.5:
      x[2] = x[2] + 1
    elif num < 2.0:
      x[3] = x[3] + 1
    elif num < 2.5:
      x[4] = x[4] + 1
    elif num < 3.0:
      x[5] = x[5] + 1
    elif num < 3.5:
      x[6] = x[6] + 1
    elif num < 4.0:
      x[7] = x[7] + 1
    elif num < 4.5:
      x[8] = x[8] + 1
    else:
      x[9] = x[9] + 1 
  print(x)

#test_m_random(8,10000)

###################################
## 1-a RANDOM.RANDOM() GENERATOR ##
###################################

def test_py_random(s,n):
# Generates n random numbers in [0,5)
# using the python built-in generator and 
# checks for uniform distribution
  x = [0 for i in range(10)]
  for i in range(n):
    r = random.random()
    num = 5 * r
    if num < 0.5:
      x[0] = x[0] + 1
    elif num < 1.0:
      x[1] = x[1] + 1
    elif num < 1.5:
      x[2] = x[2] + 1
    elif num < 2.0:
      x[3] = x[3] + 1
    elif num < 2.5:
      x[4] = x[4] + 1
    elif num < 3.0:
      x[5] = x[5] + 1
    elif num < 3.5:
      x[6] = x[6] + 1
    elif num < 4.0:
      x[7] = x[7] + 1
    elif num < 4.5:
      x[8] = x[8] + 1
    else:
      x[9] = x[9] + 1
  print(x)

#test_py_random(8,10000)

#################
## 1-b MERSENNE##
#################

def m_rand_gen(s, n):
# Generates n random numbers in [0,1]
# using the simple mersenne
  x = [0 for i in range(n)]
  k = 16807
  j = 2147483647
  count = 0
  for i in range(n):
    s = (k * s) % j
    x[i] = s / j
    r1 = random.random()
    r2 = random.random()
    if r1 < r2:
      count = count + 1
    r1 = r2
  print(count)

#m_rand_gen(8,10000)

#########################
## 1-b RANDOM.RANDOM() ##
#########################

def rand_gen(s, n):
# Generates n random numbers in [0,1)
# using the builtin generator
# with a given seed  
  x = [0 for i in range(n)]
  count = 0
  for i in range(n):
    x[i] = random.random()
    r1 = random.random()
    r2 = random.random()
    if r1 < r2:
      count = count + 1
    r1 = r2
  print(count)

#rand_gen(8,10000)



################
## Question 3 ##
################

def rand_mc(s, n):
# Generates n random numbers in [0,1)
# using the builtin generator
# with a given seed  
  x = [0 for i in range(n)]
  for i in range(n):
    x[i] = random.random()
      
  print(x)

def f(x):
  return math.exp(x)

#rand_mc(8,10000)

def gen_random_plot(s,n):
#Generates n random points using the builtin generator
#with a given seed  random.seed(s), and plots those that
#fall in the circle of radius 1
  x = [0 for i in range(n)]
  y = [0 for i in range(n)]
  i = 0
  while i < n:
    rx = 2*rn.random()-1
    ry = 2*rn.random()-1
    if abs(rx) + abs(ry) <= 1:
      x[i] = rx
      y[i] = ry
      i = i + 1
  plt.scatter(x, y)
  plt.show()

gen_random_plot(8,1000)