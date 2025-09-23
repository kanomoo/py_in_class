#นายปภาวิน ธิติชุณหกุล 6806021612037
from random import randint
while True:
    print("\nMain Menu\n==========\n 1. Play Game\n 2. Exit\n")
    choice,rd = int(input("Enter Choice : ")),randint(1,99) #ต้อง random นอก match
    match choice:
        case 1:
            print("\nNow Play game")
            for i in range(6):
                num = int(input(f"Enter guess number(#{i+1}) : "))
                if num > rd: print("Your value is more than")
                elif num < rd: print("Your value is less than")
                elif num == rd:
                    print(f"\nYou win, use guess {i} times.\nNumber guess is {rd}.")
                    break
                if i == 5: print(f"\nYou lose, random number is {rd}")
        case 2:
            print("Exit Program...\n")
            input("Press any key to continue . . .")
            break
        case _:
            print("No choice, enter again.")