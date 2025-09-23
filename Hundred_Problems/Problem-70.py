#bank account management system
def bank_account_management():
    data = 0
    while True:
        print("\nBank Account Management System\n\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Exit Program\n")
        choice = input("Select Choice : ")
        match choice:
            case "1":
                try:
                    deposit = int(input("Enter Deposit Money : "))
                    data += deposit
                except ValueError:
                    print("Please input integer")
            case "2":
                try:
                    withdraw = int(input("Enter Withdraw Money : "))
                    if withdraw <= data:
                        data -= withdraw
                    else:
                        print("Please withdraw money not over")
                except ValueError:
                    print("Please input integer")
            case "3":
                print("Your Balance : ",data)
            case "4":
                print("Exit Program")
                break
            case _:
                print("No choice")

bank_account_management()