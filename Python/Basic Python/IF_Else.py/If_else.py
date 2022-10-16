# If statement:
a = 33
b = 200

if b > a:
  print("b is greater than a")

# Elif = The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else = The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Use else without the elif
a = 300
b = 400
if a > b : 
  print("a is greater than b")
else: 
  print("a is not greater than b")

# Test if a is geater than b, AND if c is greater than a: 
c = 122
d = 45
e = 421
if c > d and e > c : 
  print("Both condition are True")

# Test a is greater than b, OR if a is greater than c: 
a = 200
b = 33
c = 5000
if a > b or a > c: 
  print("At least one if the condition is true")

# Nested if  
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
