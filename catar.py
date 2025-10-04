import math
from functools import reduce
import operator
def analyse(inputs, operation):
 if operation == '+':
  return sum(inputs)
 if operation == '-':
  return reduce(lambda x,y:x-y, inputs)
 if operation == '*':
  return reduce(operator.mul, inputs)
 if operation == '/':
  #if any( x == 0 for x in inputs[1]):
   #return "Cannot operate"
  return reduce(operator.truediv, inputs)
 if operation == '^':
  if len(inputs) > 1:
   return math.pow(inputs[0], inputs[1])
  else:
   return 'wROng eVALuatION'
 if operation == '!':
  dum = int(inputs)
  if len(inputs) > 1:
   return "ErrOR 4o4"
  return math.factorial(dum[0])
 if operation == 'P':
  n, r = int(inputs[0]), int(inputs[0])
  if len(inputs) == 2:
   return math.perm(n, r)
  else:
   return 'wROng eVALuatION'
 if operation == 'radians':
  if len(inputs) == 1:
   return math.radians(inputs[0])
  else:
   return 'ValueError'
 if operation == 'cos':
  if len(inputs) == 1:
   return math.cos(inputs[0])
  else:
   return 'ValueError'
 if operation == 'sin':
  if len(inputs) == 1:
   return math.sin(inputs[0])
  else:
   return 'ValueError'
 if operation == 'tan':
  if len(inputs) == 1:
   return math.tan(inputs[0])
 else:
   return 'ValueError'
 if operation == 'sqrt':
  if len(inputs) == 1:
   return math.sqrt(inputs[0])
 else:
   return 'ValueError'
def inputs():
 sad = None
 while True:
  extra = []
  if sad is None:
   Fig = input("Enter Fig or type 'done' to quit: ").split()
   if Fig[0].lower() == 'done':
    break
   Fig = [float(n) for n in Fig]
  else:
   Lif = input(f"\nPrevious Result {sad} \nEnter 'use' to retain memory  \ntype 'end' to end \nType 'clean' to clean memory: ")
   if Lif == 'end':
    break
   elif Lif == 'clean':
    sad = None
    continue
   elif Lif == 'use':
    Fig = [sad]
   extra= input(" Enter Fig(s) or type 'done': ").split()
   if extra[0].lower() == 'done':
    break
  #if extra.split():
   Fig += [float(n) for n in extra]
  while True:
   print(" Operations: \n+ \n- \n* \n/ \n! \nP \nradians \ncos \nsin \ntan \nsqrt \nnew \nmem \nquit")
   value = input('Choose Operation:' )
   if value == 'quit':
    return
   elif value == 'new':
    sad = None
    break
   elif value in ['sqrt', 'sin', 'cos', 'tan', '!', 'radians']:
    if extra:
     jef = extra[:]
   else:
    jef = Fig
    sad = analyse(jef, value)
    print(sad)
    mem = input('Type again to try another op on SAME nums, or press Enter to move on: ')
    if mem == 'again':
     break
inputs()   
           
 