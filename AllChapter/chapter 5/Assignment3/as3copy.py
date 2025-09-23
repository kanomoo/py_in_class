head, salary, discount, result = "| Tax Main Menu |", 0, 100000, ""
line = "=" * len(head)
while True:
    print(line,head,line,sep="\n")
    print(f" 0. Exit\n 1. Input Salary({salary:,.2f})\n 2. Display Tax")
    choice = int(input("Enter choice : "))
    match choice:
        case 0:
            print("\nExit Program . . .")
            break
        case 1: salary = int(input("Enter salary : "))
        case 2:
            income  = salary * 12
            net_income = income - discount
            print(f"Salary :  {salary:,.2f}\nIncome :  {income:,.2f}\nDiscount :  {discount:,.2f}\nNet income :  {net_income:,.2f}\n\nReport Tax:")
            line2 = "=" * 78
            head2 = f"|         Net     Income      |Tax Rate|{"Tax":^37}|"
            print(line2,head2,line2,sep="\n")
            if net_income >= 1 :
                NET,INCOME,TR,PRICE,NET_INCOME ,TNC, total = 1,150000,0,0,net_income,0, 0
                if NET_INCOME >= INCOME:
                    SHOW = INCOME
                    NET_INCOME -= INCOME
                else: SHOW = NET_INCOME
                TAX = f" {SHOW:,.2f} * {TR:.2f}"
                PRICE = SHOW * PRICE
                total += PRICE
                print(f"| {NET:>12,.2f} - {INCOME:>12,.2f} |   {TR:>2}%  |{TAX:21} |{PRICE:13,.2f} |")
            if net_income >= 150001 :
                NET,INCOME,TR,PRICE = 150001,300000,5,0.05
                if NET_INCOME >= INCOME - NET+1:
                    SHOW = INCOME - NET+1
                    NET_INCOME -= INCOME - NET+1
                else: SHOW = NET_INCOME
                TAX = f" {SHOW:,.2f} * {TR:.2f}"
                PRICE = SHOW * PRICE
                total += PRICE
                print(f"| {NET:>12,.2f} - {INCOME:>12,.2f} |   {TR:>2}%  |{TAX:21} |{PRICE:13,.2f} |")
            if net_income >= 300001 :
                NET,INCOME,TR,PRICE = 300001,500000,10,0.10
                if NET_INCOME >= INCOME - NET+1:
                    SHOW = INCOME - NET+1
                    NET_INCOME -= INCOME - NET+1
                else: SHOW = NET_INCOME
                TAX = f" {SHOW:,.2f} * {TR:.2f}"
                PRICE = SHOW * PRICE
                total += PRICE
                print(f"| {NET:>12,.2f} - {INCOME:>12,.2f} |   {TR:>2}%  |{TAX:21} |{PRICE:13,.2f} |")
            if net_income >= 500001 :
                NET,INCOME,TR,PRICE = 500001,750000,15,0.15
                if NET_INCOME >= INCOME - NET+1:
                    SHOW = INCOME - NET+1
                    NET_INCOME -= INCOME - NET+1
                else: SHOW = NET_INCOME
                TAX = f" {SHOW:,.2f} * {TR:.2f}"
                PRICE = SHOW * PRICE
                total += PRICE
                print(f"| {NET:>12,.2f} - {INCOME:>12,.2f} |   {TR:>2}%  |{TAX:21} |{PRICE:13,.2f} |")
            if net_income >= 750001 :
                NET,INCOME,TR,PRICE = 750001,1000000,20,0.20
                if NET_INCOME >= INCOME - NET+1:
                    SHOW = INCOME - NET+1
                    NET_INCOME -= INCOME - NET+1
                else: SHOW = NET_INCOME
                TAX = f" {SHOW:,.2f} * {TR:.2f}"
                PRICE = SHOW * PRICE
                total += PRICE
                print(f"| {NET:>12,.2f} - {INCOME:>12,.2f} |   {TR:>2}%  |{TAX:21} |{PRICE:13,.2f} |")
            if net_income >= 1000001 :
                NET,INCOME,TR,PRICE = 1000001,2000000,25,0.25
                if NET_INCOME >= INCOME - NET+1:
                    SHOW = INCOME - NET+1
                    NET_INCOME -= INCOME - NET+1
                else: SHOW = NET_INCOME
                TAX = f" {SHOW:,.2f} * {TR:.2f}"
                PRICE = SHOW * PRICE
                total += PRICE
                print(f"| {NET:>12,.2f} - {INCOME:>12,.2f} |   {TR:>2}%  |{TAX:21} |{PRICE:13,.2f} |")
            if net_income >= 2000001 :
                NET,INCOME,TR,PRICE = 2000001,5000000,30,0.30
                if NET_INCOME >= INCOME - NET+1:
                    SHOW = INCOME - NET+1
                    NET_INCOME -= INCOME - NET+1
                else: SHOW = NET_INCOME
                TAX = f" {SHOW:,.2f} * {TR:.2f}"
                PRICE = SHOW * PRICE
                total += PRICE
                print(f"| {NET:>12,.2f} - {INCOME:>12,.2f} |   {TR:>2}%  |{TAX:21} |{PRICE:13,.2f} |")
            if net_income >= 5000001 :
                NET,INCOME,TR,PRICE = 0,5000000,35,0.35
                if NET_INCOME >= INCOME - (NET+1):
                    SHOW = INCOME - (NET+1  )
                    NET_INCOME -= INCOME - (NET+1)
                else: SHOW = NET_INCOME         
                TAX = f" {SHOW:,.2f} * {TR:.2f}"
                PRICE = SHOW * PRICE
                total += PRICE
                print(f"| {"":>12} > {INCOME:>12,.2f} |   {TR:>2}%  |{TAX:21} |{PRICE:13,.2f} |")
            print(line2)
            print(f"|{"Total":^61}|{total:13,.2f} |")
            print(line2)
    print()