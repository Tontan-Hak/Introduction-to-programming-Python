fav_movies = [1,5,7,3,4.5,True, "Moon man"]
print(fav_movies[6])
# Make the favorite numbers
fav_numbers = [3,8,12]
print(fav_numbers[2])

# Upper case
A = "hello world"
print(A.upper())

# Lower Case
a = "Hello crush"
print(a.lower())

# Remove Whitespace
b = " I love you! "
print(b.strip()) # return "I love you!"

# Replace string
c = "Tontan Hak"
print(c.replace("Ton", "Ly"))

# Split string
d = "Hello, World!"
e = d.split(",")
print(e)

# String Cancatenation
f = "Lytan"
g = "Hak"
h = f + " " + g
print(h)

# String format 
age = 24
txt = "My name is Tontan, and I am {} years old"
print(txt.format(age))

# 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Use {0}
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))