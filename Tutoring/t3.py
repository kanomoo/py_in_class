while True:
    choice = input("Programm Test Call Module\nMain Menu\n1. Find Max Number\n2. Check Palindrome\n3. Number to Text\n4. Decimal to Binary\n5. Exit\nEnter choice : ")
    match choice:
        case "1":
            num = input("Enter number : ")
            print(f"Maximum digit {max(str(num))} of number {num}")
        case "2":
            num = input("Enter number : ")
            if num == num[::-1]: print(f"Number {num} is Palindrome.")
            else: print(f"Number {num} is Not Palindrome.")
        case "3":
            num = input("Enter number : ")
            text = {"0":" Zero", "1":" One", "2":" Two", "3":" Three", "4":" Four", "5":" Five", "6":" Six", "7":" Seven", "8":" Eight", "9":" Nine"}
            result = "Text :"
            for i in num:
                if i in text: result += text[i]
            print(result)
        case "4":
            num = int(input("Enter decimal number : "))
            print(f"Decimal number : {num}\nBinary number : {bin(num)[2:]}")
        case "5":
            print("Exit Program.")
            exit()
    print()