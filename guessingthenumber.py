import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess < number:
        print("Too low, try again!")
    elif guess > number:
        print("Too high, try again!")
    else:
        print("Congratulations, you guessed the number!")
        break
