# ชือ (งานนี้ 34 คะแนน)
head = ">> Program Calculator <<"
line = len(head) * "="
while True:
    print(line,head,line,f"|{" 1. Input qty":22}|\n|{" 2. Reprit input":22}|\n|{" 3. Report Price":22}|\n|{" 4. Exit":22}|",line,sep="\n")
    choice,result = int(input("Select Choice : ")), ""
    match choice:
        case 1:
            a,pa = int(input("\nEnter Qty A : ")), 1200
            b,pb = int(input("Enter Qty B : ")), 400
            c,pc = int(input("Enter Qty C : ")), 300
            d,pd = int(input("Enter Qty D : ")), 150
        case 2:
            h = f"|No.|{"Price":^14}|{"Qty":^14}|{"Total":^14}|"
            l = "=" * (len(h))
            result += f"| 1 | {pa:12,.2f} | {a:12,.2f} | {pa * a:12,.2f} |\n"
            result += f"| 2 | {pb:12,.2f} | {b:12,.2f} | {pb * b:12,.2f} |\n"
            result += f"| 3 | {pc:12,.2f} | {c:12,.2f} | {pc * c:12,.2f} |\n"
            result += f"| 4 | {pd:12,.2f} | {d:12,.2f} | {pd * d:12,.2f} |\n"
            tq = sum((a,b,c,d))
            total = (pa * a)+(pb * b)+(pc * c)+(pd * d)
            if total >= 100000: vat = 8
            elif total >= 750000: vat = 7.5
            elif total >= 500000: vat = 6
            elif total >= 250000: vat = 5.5
            elif total >= 100000: vat = 2
            elif total >= 50000: vat = 1.5
            elif total >= 0 : vat = 1
            print("",l,h,l,result+l,sep="\n")
        case 3:
            h2 = f"+{"=" * 26}+"
            print("",h2, f"| Total Qty   |{tq:11,.2f} |",sep="\n")
            print(h2, f"| Total Price |{total:11,.2f} |", sep="\n")
            print(h2, f"| Per Vat     |{vat:10,.2f}% |", sep="\n")
            print(h2, f"| Total Vat   |{total * vat/100:11,.2f} |", sep="\n")
            print(h2, f"| Total       |{total + total * vat/100:11,.2f} |",h2, sep="\n")
        case 4:
            print("\nExit Program...")
            break
        case _:
            print("\nNo choice")
    print()