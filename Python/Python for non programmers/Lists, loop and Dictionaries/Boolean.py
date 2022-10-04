# Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Boolean
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))