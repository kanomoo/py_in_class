# number guessing game
from random import randint
def number_guessing_game() -> None:
    while True:
        score = randint(1, 100)
        print("\nMenu:\n1. Start New Game\n2. Show instructions\n3. Exit\n")
        choice = input("Please select an option : ")
        match choice:
            case "1":
                n = 0
                while True:
                    try:
                        n += 1
                        num = int(input("Guess a number between 1 and 100: "))
                        print("Please input int")
                        if num > score:
                            print("Your guess is too high. Try again!")
                        elif num < score:
                            print("Your guess is too low. Try again!")
                        else:
                            print(f"Congratulations! You guessed the number correctly in {n} attempts.\n\nReturning to main menu..")
                            break
                    except ValueError: 
                        print("Please input integer")
            case "2":
                print("\nWelcome to the Number Guessing Game! "
                      "\n1. The system will randomly select a number between 1 and 100."
                      "\n2. Your task is to guess the number."
                      "\n3. After each guess, you will be informed if your guess is too high, too low, orcorrect."
                      "\n4. Keep guessing until you find the correct number."
                      "\n5. The game will show you the number of attempts you took to guess thenumber.")
            case "3":
                print("\nThank you for playing! Goodbye!")
                break

number_guessing_game()
