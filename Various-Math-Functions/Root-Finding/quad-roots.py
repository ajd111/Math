import math 

def quad_roots(a,b,c):
  a 
  b 
  c    
  print("The solution to ax^2 + bx + c = 0:")
  if a == 0:
    print("This function is not a quadratic")
    return
  if b == 0:
    if c == 0:
      print("x = 0") 
    elif (c > 0):
      print("No real roots")
    else:
     math.sqrt(-c/a)
  else:
    disc = b**2 - 4*a*c
    if (disc < 0):
      print("This equation has no real solution")
    else:
      if b > 0:
        print("If b is greater than zero, then we either use the standard form, -b - sqrt(b^2 - 4ac) / 2a, or the rationalized form 2c / -b - sqrt(b^2 - 4ac)")
      else:
        print("If b is less than zero, then we either use the standard form, -b + sqrt(b^2 - 4ac) / 2a, or the rationalized form 2c / -b + sqrt(b^2 - 4ac)")
    

#quad_roots(-9,9,-9)