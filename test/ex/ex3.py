head = "| Tax Main Menu |"
line, salary, = "=" * len(head), 0
while True:
    print(line,head,line,f" 0. Exit\n 1. Input Salary({salary:,.2f})\n 2. Display Tax",sep="\n")
    choice = int(input("Enter choice : "))
    match choice:
        case 0:
            print("\nExit Program...")
            break
        case 1: salary = int(input("Enter salary : "))
        case 2:
            net_income = salary * 12 - 100000
            print(f"\nSalary :  {salary:,.2f}\nIncome :  {salary * 12:,.2f}\nDiscount :  {100000:,.2f}\nNet Income : {net_income:,.2f}\n\nReport Tax:")
            h = f"|         Net     Income       |Tax Rate|{"Tax":^{len("         Net      Income     |Tax Rate")}}|"
            l, tp = len(h) * "=", 0
            print(l,h,l,sep="\n")
            for i in range(8):
                if i == 0 :   net, income, tr, tax, price =       1,  150000,  0, "", 0
                elif i == 1 : net, income, tr, tax, price =  150001,  300000,  5, "", 0
                elif i == 2 : net, income, tr, tax, price =  300001,  500000, 10, "", 0
                elif i == 3 : net, income, tr, tax, price =  500001,  750000, 15, "", 0
                elif i == 4 : net, income, tr, tax, price =  750001, 1000000, 20, "", 0
                elif i == 5 : net, income, tr, tax, price = 1000001, 2000000, 25, "", 0
                elif i == 6 : net, income, tr, tax, price = 2000001, 5000000, 30, "", 0
                elif i == 7 : net, income, tr, tax, price =       0, 5000001, 35, "", 0
                if net_income > (income - net) : show = (income - net+1)
                else: show =  net_income
                if i == 7: show = net_income
                tax = f" {show:,.2f} * {tr / 100:.2f}"
                price = show * tr / 100
                net_income -= show
                tp += price
                if net != 0: print(f"|{net:>{len("          Net ")},.2f} -{income:>{len("ncome        ")},.2f} |   {tr:2}%  |{tax:<{len("                Tax   ")}}|{price:>{len("              ")},.2f} |")
                else: print(f"|{"":>{len("          Net ")}} >{income:>{len("ncome        ")},.2f} |   {tr:2}%  |{tax:<{len("                Tax   ")}}|{price:>{len("              ")},.2f} |")
                if net_income == 0: break
            print(l,f"|{"Total Tax":^{len("         Net     Income      |Tax Rate|                  Tax  ")}}|{tp:>{len("              ")},.2f} |",l,sep="\n")
    print()