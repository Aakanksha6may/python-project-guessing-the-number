# python-project-guessing-the-number
This is python project - guessing the number . a program that generates a random number between 1 and 100 and allows the user to guess the number until they get it right.

Here are the steps to create this project:

Step 1: Install Python

Before you can start writing Python code, you need to install Python on your computer. You can download the latest version of Python from the official website: https://www.python.org/downloads/. Follow the instructions to install Python on your computer.

Step 2: Open a Text Editor

To write your Python code, you need a text editor. You can use any text editor you like, but some popular options include Visual Studio Code, Sublime Text, and Atom. Open your text editor and create a new file.

Step 3: Write the Code

Copy and paste the following code into your text editor:

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
        
        
This code imports the random module, which we'll use to generate a random number between 1 and 100. The code then enters a while loop that continues until the user guesses the correct number.

Inside the loop, the code prompts the user to enter a guess using the input function. We convert the user's input to an integer using the int function.

If the user's guess is lower than the random number, the code prints "Too low, try again!" If the user's guess is higher than the random number, the code prints "Too high, try again!" If the user's guess is correct, the code prints "Congratulations, you guessed the number!" and exits the loop using the break keyword.

Step 4: Save and Run the Code

Save your Python file with a .py extension (e.g. guessing_game.py). Then open a terminal or command prompt and navigate to the directory where you saved the file. Run the code by typing python guessing_game.py and pressing enter.

The program will generate a random number and prompt you to guess the number. Keep guessing until you get it right!
