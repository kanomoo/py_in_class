head = "        Drinks menu      "
line, result, total, n = len(head) * "=", "", 0, 0
while True:
    print(line,head,line,sep="\n")
    print(f"| {"0. Quit":22}|\n| {"1. Hot Coffee":22}|\n| {"2. Ice Coffee":22}|\n| {"3. Frappe Coffee":22}|\n| {"4. Caculate Cost":22}|",line,sep="\n")
    choice = int(input("Select Item : "))
    match choice:
        case 0:
            print("Exit Program...")
            break
        case 1:
            hot = int(input("Hot Coffee, how many glasses : "))
            result += f"{hot} {"Hot Coffee":15}30.00 {30*hot:6.2f}\n"
            total += 30*hot
        case 2:
            ice = int(input("Ice Coffee, how many glasses : "))
            result += f"{ice} {"Ice Coffee":15}35.00 {35 * ice:6.2f}\n"
            total += 35 * ice
        case 3:
            frappe = int(input("Frappe Coffee, how many glasses : "))
            result += f"{frappe} {"frappe Coffee":15}50.00 {50 * frappe:6.2f}\n"
            total += 50 * frappe
        case 4:
            n += 1
            print(f"\nOrder #{n}")
            h = "Qty Item        Price   Total"
            l = len(h) * "-"
            print(l,h,l,result+l,f"Total: {total:.2f} Bath",sep="\n")
            result = ""
            total = 0
        case _: print("No Choice")
    print()