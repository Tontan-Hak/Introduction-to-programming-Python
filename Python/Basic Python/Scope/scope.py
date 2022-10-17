# A variable created inside a function is available inside that function:
def myfunc():
  x = 300
  print(x)

myfunc()

# The local variable can be accessed from a function within the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# A variable created outside of a function is global and can be used by anyone:
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
