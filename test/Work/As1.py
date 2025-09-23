#ข้อ 1 สันติชัย ไชยมโน 6806021612401
from random import  randint
while True:
    print("Main Menu\n============\n 1. Play Game\n 2. Exit")
    choice = int(input("Enter Choice : "))
    match choice:
        case 1:
            score = randint(1,99)
            print("\nNow Play game")
            for i in range(6):
                value = int(input(f"Enter guess number(#{i}) : "))
                if value > score: print("Your value is more than")
                elif value < score: print("You value is less than")
                elif value == score:
                    print(f"\nYou win, use guess {i} times.\nNumber guess is {score}.")
                    break
            else: print(f"\nYou lose, random number is {score}.")
        case 2:
            print("Exit Program...")
            break
        case _:
            print("No Choice, enter again.")
    print()
print("\nPress any key to continue . . .")