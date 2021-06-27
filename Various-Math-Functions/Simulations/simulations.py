import random
import math

##############
# Question 1 #
##############
def loaded(n):
  x = [0 for i in range(6)]
  for i in range(n):
    r = random.random()
    if r < 0.15:
      x[0] = x[0] + 1
    elif r < 0.35:
      x[1] = x[1] + 1
    elif r < 0.6:
      x[2] = x[2] + 1
    elif r < 0.75:
      x[3] = x[3] + 1
    elif r < 0.85:
      x[4] = x[4] + 1
    else:
      x[5] = x[5] + 1
  print("The probability of getting a 1, 2, 3, 4, 5, or 6 using a loaded die:")
  print(x[0]/n, x[1]/n, x[2]/n, x[3]/n, x[4]/n, x[5]/n)

#loaded(10000)

##############
# Question 2 #
##############
def double6(n):
  count = 0
  for i in range(n):
    found = "no"
    for i in range(25):
      d1 = random.randint(1, 6)
      d2 = random.randint(1, 6)
      if d1 * d2 == 36:
        found = "yes"
      if found == "yes":
        count = count + 1 
  print("The percentage of the time a double 6 was rolled:")
  print((count/n)*100)

#double6(10000)

##############
# Question 3 #
##############
def buffon(n):
  count = 0
  for i in range(n):
    u = 0.5 * random.random()
    v = 1.57079632679490 * random.random()
    if u < ((1/2) * math.sin(v)):
      count = count + 1
  print(count/n)
  print(2/count)

#buffon(100000)

##############
# Question 4 #
##############
def drunk(n):
  count = 0
  for i in range(n):
    x = 0
    y = 0
    for i in range(51):
      r = random.random()
      if r < 0.16666666667:
       x = x + 1
      if r < 0.4166666667:
        y = y + 1
      elif r < 0.6666666667:
        y = y - 1
      else:
        x = x - 1
    if x**2 + y**2 == 20**2:
      count = count + 1
  print((count/n) * 100)

#drunk(1000)