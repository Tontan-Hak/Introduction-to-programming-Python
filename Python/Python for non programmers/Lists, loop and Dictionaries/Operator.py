# returns True because 5 is greater than 3 AND 5 is less than 10
x = 5
print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
x = 21
print(x > 3 and x < 10)

# 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
