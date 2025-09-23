head = (">>  Main Menu  <<<")
line, price, payment, py, month = len(head) * "=", 0, 0, 0, 0
while True:
    print(head,line,f" 0. Exit Program\n 1. Input Car Price ({price:,.2f})\n 2. input Down Payment ({payment:,.2f}%)\n"
                    f" 3. input Interest [Per Year] ({py:,.2f}%)\n 4. input Month Number({month})\n 5. Display Installment\n 6. Clear All Data",sep="\n")
    choice = int(input("Select choice : "))
    match choice:
        case 0:
            print("Exit Program...")
            break
        case 1:
            price = int(input("Enter car price : "))
        case 2:
            payment = float(input("Enter down payment(%) : "))
        case 3:
            py = float(input("Enter interest( %) per year : "))
        case 4:
            month = int(input("Enter month : "))
        case 5:
            print(f"\nPrice car : {price:,.2f}\nAmount down payment({payment:,.2f}%) : {price * payment//100:,.2f}\n"
                  f"Amount finance : {price - (price * payment//100):,.2f}\nAmount interest({py:,.2f}%) : {(price - (price * payment//100)) * ((py/12)/100) * month:,.2f}\n"
                  f"Amount net finance : {(price - (price * payment//100)) + (price - (price * payment//100)) * ((py/12)/100) * month:,.2f}\n"
                  f"Amount installment(per month) : {((price - (price * payment//100)) + (price - (price * payment//100)) * ((py/12)/100) * month) / 60:,.2f}")
        case 6:
            price, payment, py, month = 0, 0, 0, 0
    print()