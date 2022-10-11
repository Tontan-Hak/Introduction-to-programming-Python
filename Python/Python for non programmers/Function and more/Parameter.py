# Parameter
from audioop import add
from unicodedata import name


def hello(name): 
    print(f"Hello {name}!")
hello("Vita") 

def add_numbers(num1,num2):
    print(num1 + num2)
add_numbers(4,8)
add_numbers(4,7)

# Create a function called dog_info takes in a dog's age and name prints a sentence about the dog
def dog_info(age,name):
    print(f"Hey, I am {name}, and I am {age} years old")
dog_info(5,"Moli")