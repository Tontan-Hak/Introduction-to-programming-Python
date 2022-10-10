# Globle variable 
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Global Variable 
x = "Awesome"
def myfunc():
    x = "Fantastic"
    print("Python is " +x)

myfunc()
print("Python is " +x)

# The global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)