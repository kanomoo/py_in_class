print("Show Menu\n===========")
print("1. Menu 1\n2. Menu 2\n3. Menu 3\n4. Exit")
choice = input("Enter choice : ")
match choice:
    case "1":
        print("Choose 1")
    case "2":
        print("Choose 2")
    case "3":
        print("Choose 3")
    case "4":
        print("Choose Exit")
    case _:
        print("Error no choice")

