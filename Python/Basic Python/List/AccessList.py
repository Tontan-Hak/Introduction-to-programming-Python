# Access Item
fruit = ["Banana", "apply", "Anana", "Cherry"]
print(fruit[3])

# 
Fruit = ["Apple", "Banana", "Cherry", "Anana", "Kiwi", "Melon", "Mango"]
print(Fruit[2:5])

# This will return the items from index 0 to index 4
# Remember that index 0 is the fist item, and index 4 is th fifth item
# Remember that the item in index 4 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if item Exists
Thislist = ["Apple", "Banana", "Cerry"]
if "Apple" in Thislist: 
    print("Yes, 'Apple' is in the Fruit list")

# Change Item Value
thislist = ["Banana", "Apple", "Papaya"]
thislist[1] = "Durren"
print(thislist)

# Change Item List
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items
fruit = ["apple", "banana","anana"]
fruit.insert(2, "watermelon")
print(fruit)

# Extend List
thislist = ["A", "B", "C"]
tropical = ["D", "E", "F"]
thislist.extend(tropical)
print(thislist)
