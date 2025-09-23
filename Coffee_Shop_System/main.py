def menu():
    while True:
        choice = input(f"{"\nCoffee Menu":^12}\n{"=" * 11}\n1. Add Menu Coffee\n2. Report Menu Coffee\n"
              f"3. Back to Main\n\nSelect choice : ")
        match choice:
            case "1":
                with open("Coffee_Menu.txt","a") as fout:
                    name = input("\nName : ")
                    price = int(input("Price : "))
                    fout.write(f"{name} {price}\n")
            case "2":
                with open("Coffee_Menu.txt",encoding = "UTF-8") as fin:
                    print(fin.read())
            case "3":
                pass

menu()