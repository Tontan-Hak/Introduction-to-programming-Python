# Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Length
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Access Tuple
Fruits = ("apple", "banana","cherry")
print(Fruits[2])

#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# By leaving out the end value, the range will go on to the end of the list:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Convert the tuple into a list to be able to change it:
x =("apple", "banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Using loop throught tuple
fruit = ("apple","banana", "cherry")
for x in fruit:
    print(x)

# Join the two tuple
tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)