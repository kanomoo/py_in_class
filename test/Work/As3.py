#ข้อ 3 สันติชัย ไชยมโน 6806021612401
head = "| Tax Main Menu |"
line,salary = len(head) * "=", 0,
while True:
    print(line,head,line,f" 0. Exit\n 1. Input Salary({salary:,.2f})\n 2. Display Tax",sep="\n")
    choice,result, total = int(input("Enter choice : ")), "", 0
    match choice:
        case 0:
            print("\nExit Program ...")
            break
        case 1:
            salary = int(input("Enter salary : "))
        case 2:
            net_income = salary * 12 - 100000
            print(f"\nSalary :  {salary:,.2f}\nIncome :  {salary*12:,.2f}\nDiscount :  {100000:,.2f}\nNet Income :  {net_income:,.2f}\n\nReport Tax:")
            for i in range(8):
                if i == 0:   net, income, tax_rate, tax, show =       1,  150000,  0, "", 0
                elif i == 1: net, income, tax_rate, tax, show =  150001,  300000,  5, "", 0
                elif i == 2: net, income, tax_rate, tax, show =  300001,  500000, 10, "", 0
                elif i == 3: net, income, tax_rate, tax, show =  500001,  750000, 15, "", 0
                elif i == 4: net, income, tax_rate, tax, show =  750001, 1000000, 20, "", 0
                elif i == 5: net, income, tax_rate, tax, show = 1000001, 2000000, 25, "", 0
                elif i == 6: net, income, tax_rate, tax, show = 2000001, 5000000, 30, "", 0
                elif i == 7: net, income, tax_rate, tax, show =       0, 5050001, 35, "", 0
                if net_income > income - (net+1): show = income - (net-1)
                else: show = net_income
                if net_income == 0 : break
                net_income -= show
                total += show * tax_rate/100
                if net > 0 : result += f"|{net:13,.2f} -{income:13,.2f} |   {tax_rate:2}%  | {f"{show:,.2f} * {tax_rate/100:.2f}":22}|{show * tax_rate/100:15,.2f} |\n"
                else: result += f"|{"":13} >{income:13,.2f} |   {tax_rate:2}%  | {f"{show:,.2f} * {tax_rate/100:.2f}":22}|{show * tax_rate/100:15,.2f} |\n"
            h = f"|         Net     Income      |Tax Rate|{"Tax":^40}|"
            l = len(h) * "="
            print(l,h,l,result+l,f"|{"Total Tax":^62}|{total:15,.2f} |",l,sep="\n")
        case _ : print("No Choice...")
    print()