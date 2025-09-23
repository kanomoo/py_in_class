while True:
    line = "+" + "-" * 38 + "+"
    print(line,f"|{"Currency Convert":^38}|",line,f"|{"0.Exit":<38}|",f"|{"1.Enter money":<38}|",f"|{"2.Convert THB to USD(33 THB / 1 USD)":<38}|",f"|{"3.Convert THB to JPY(0.2 THB / 1 JPY)":<38}|",f"|{"4.Convert THB to EUR(37 THB / 1 EUR)":<38}|",line,sep="\n")
    choice = int(input("Enter choice : "))
    match choice:
        case 0: 
            print("exit.")
            break
        case 1:
            num = int(input("Enter money : "))
            print(f"your money :{num:,.2f} (THB)")
        case 2: print(f"{num:,.2f}(THB) => {num / 33:,.2f}(USD)")
        case 3: print(f"{num:,.2f}(THB) => {num / 0.2:,.2f}(JPY)")
        case 4: print(f"{num:,.2f}(THB) => {num / 37:,.2f}(EUR)")
        case _: print("No choice pleace try again.")        