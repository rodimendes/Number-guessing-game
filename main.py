import random
import art

def easy_game(hide_number):
    guessed_numbers = []
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    while not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
        guess = input("Please, hit a valid number: ")
    guess = int(guess)
    while guess != hide_number and attempts > 1:
        guessed_numbers.append(guess)
        attempts -= 1
        if guess < hide_number:
            print("\nToo low.")
        else:
            print("\nToo high.")
        print(f"You have {attempts} attempts remainig to guess the number and guessed the numbers {guessed_numbers}")
        if attempts <= 3:
            print(f"You only have {attempts} and the first number is {number // 10}.")
        guess = input("Guess again: ")
        while not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
            guess = input("Please, hit a valid number: ")
        guess = int(guess)
        while guess in guessed_numbers:
            guess = input("Please, hit a new number: ")
            while not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
                guess = input("Please, hit a valid number: ")
            guess = int(guess)

    if guess == hide_number:
        print(f"You win! The number was {hide_number}\nEnd of the game")
    else:
        print(f"You lose! The number was {hide_number}\nEnd of the game")


def medium_game(hide_number):
    guessed_numbers = []
    attempts = 7
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    while not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
        guess = input("Please, hit a valid number: ")
    guess = int(guess)
    while guess != hide_number and attempts > 1:         
        guessed_numbers.append(guess)
        attempts -= 1
        if guess < hide_number:
            print("Too low.")
        else:
            print("Too high.")
        print(f"You have {attempts} attempts remainig to guess the number and guessed the numbers {guessed_numbers}")
        guess = input("Guess again: ")
        while not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
            guess = input("Please, hit a valid number: ")
        guess = int(guess)
        while guess in guessed_numbers:
            guess = input("Please, hit a new number: ")
            while not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
                guess = input("Please, hit a valid number: ")
            guess = int(guess)

    if guess == hide_number:
        print(f"You win! The number was {hide_number}\nEnd of the game")
    else:
        print(f"You lose! The number was {hide_number}\nEnd of the game")


def hard_game(hide_number):
    guessed_numbers = []
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    while not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
        guess = input("Please, hit a valid number: ")
    guess = int(guess)
    while guess != hide_number and attempts > 1:         
        guessed_numbers.append(guess)
        attempts -= 1
        if guess < hide_number:
            print("Too low.")
        else:
            print("Too high.")
        print(f"You have {attempts} attempts remainig to guess the number and guessed the numbers {guessed_numbers}")
        guess = input("Guess again: ")
        while not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
            guess = input("Please, hit a valid number: ")
        guess = int(guess)
        while guess in guessed_numbers:
            guess = input("Please, hit a new number: ")
            while not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
                guess = input("Please, hit a valid number: ")
            guess = int(guess)

    if guess == hide_number:
        print(f"You win! The number was {hide_number}\nEnd of the game")
    else:
        print(f"You lose! The number was {hide_number}\nEnd of the game")



print(art.logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1, 101)

difficulty_level = input("Chose a difficulty. Type 'easy', 'medium' or 'hard':\n").lower()
while difficulty_level not in "easymediumhard":
    difficulty_level = input("Chose a difficulty. Type 'easy', 'medium' or 'hard':\n").lower()
if difficulty_level == "easy":
    easy_game(number)
elif difficulty_level == "medium":
    medium_game(number)
else:
    hard_game(number)