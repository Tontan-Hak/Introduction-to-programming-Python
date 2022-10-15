# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# To add one item to a set the add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("papaya")
print(thisset)

# Updated
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# use pop() to remove 
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal