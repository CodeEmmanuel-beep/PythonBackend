import math
from functools import reduce
import operator
def calculator (Numbers, solve):
 if solve == '+':
  return sum(Numbers)
 elif solve == '-':
  return reduce(lambda x,y: x-y, Numbers)
 elif solve == '*':
  return reduce (operator.mul, Numbers)
 elif  solve == '/':
  if 0 in Numbers[1:]:
    return None
  return reduce (operator.truediv, Numbers)
 elif solve == '!':
  num = int(Numbers[0])
  if len(Numbers) != 1:
    return None
  return math.factorial(num)
 elif solve == "p":
  n,r = int(Numbers[0]), int(Numbers[1])
  if n < r or r < 0 or n == 0:
    return "INVALID"
  return math.perm(n, r)
 elif solve == '^':
  if Numbers[0] == 0:
    return None 
  return math.pow(Numbers[0], Numbers[1])
 elif solve == 'cos':
  if len(Numbers) != 1:
   return "eRRor"
  return math.cos(Numbers[0])
 elif solve == 'tan':
  if len(Numbers) != 1:
   return "eRRor"
  return math.tan(Numbers[0])
 elif solve == 'sin':
  if len(Numbers) != 1:
   return "eRRor"
  return math.sin(Numbers[0])
 elif solve == 'radian':
  if len(Numbers) != 1:
   return "eRRor"
  return math.radians(Numbers[0])
 elif solve == 'sqrt':
  if len(Numbers) != 1:
   return 'eRRor'
  return math.sqrt(Numbers[0]) 
 else:
  return "404 nOt fOUnd"
result = None
while True:
 if result is None:
  Numb = input("Enter Fig(s) or type exit to quit: ").split()
  if Numb[0].lower() == 'exit':
   break
  Numb = [float(n) for n in Numb]
  print(f"OPERATIONS: \n+ \n- \n* \n/ \n^ \ncos \ntan \nsin \nradian \nsqrt \n! \np")
  solve = input('Choose Operation: ')
 else:
   temp = input(f"\nPrevious Result {result}\nEnter new fig: ").split()
   if temp[0].lower() == 'exit':
    break
   print(f"OPERATIONS: \n+ \n- \n* \n/ \n^ \ncos \ntan \nsin \nradian \nsqrt \n! \np")
   solve = input('Choose Operation: ')
   if solve in ['sqrt', 'sin', 'cos', 'tan', '!', 'radian']:
    Numb = [float(n) for n in temp]
   else:
    Numb = [result] + [float(n) for n in temp]
 result = calculator(Numb, solve)
 print (result)
 
  
  
   
  