# Number Guesser
import random
import time

print("Hello! Welcome to the guessing game. I am going to pick the number between 1 and 100")
time.sleep(1)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1
while guess != correct_number:
    time.sleep(2)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong, you need to guess higher. What is your guess?: "))
    else:
        guess = int(input("Wrong, you need to guess lower. What is your guess?: "))
print(f"The right answer was {correct_number}, It took you {guess_count} guesses :)")