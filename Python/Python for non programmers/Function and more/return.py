# Return functions
from tkinter.font import names
from unicodedata import name


def double(number):
    return number * 4
new_number = double(5)
print(new_number)

# Create a function that returns a string in all caps (you'll have to google this)
def uppercase(text):
    return text.upper()
print(uppercase("nick"))
names = ["Tontan", "Maly", "Rum"]
for name in names:
    print(uppercase(name))