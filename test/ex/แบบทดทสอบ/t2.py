# head = ": Program Cal Vat :"
# line, result, ta, tv, ts, Max, Min = f"+{(len(head)-2) * "="}+","", 0, 0, 0, 0, 1000000
# print(line,head,line,sep="\n")
# for i in range(7):
#     amount = int(input(f"Enter amount of day {i+1} : "))
#     sales = amount / 1.07
#     vat = amount - sales
#     ta += amount
#     ts += sales
#     tv += vat
#     if amount > Max : Max = amount
#     if amount < Min : Min = amount
#     result += f"|  {i+1}  |{amount:>{len("     Amounts  ")},.2f} |{vat:>{len("    Vat(7%)   |")},.2f} |{sales:>{len("    Sales    ")},.2f} |\n"
# h = "| day |     Amounts   |    Vat(7%)    |     Sales     |"
# l = f"+{(len(h)-2) * "="}+"
# print(f"\n{"Report Sale of Fitm shop":^{len(h)}}",l,h,l,result+l,sep="\n")
# print(f"|Total|{ta:>{len("          1.00")},.2f} |{tv:>{len("           0.07")},.2f} |{ts:>{len("         0.93")},.2f} |",l,sep="\n")
# print(f"Maximum Amount :    {Max:,.2f}\nMinimum Amount :    {Min:,.2f}\n")

head = ": Program Cal Vat :"
line, result, ta, tv, ts, Max, Min = f"+{(len(head)-2) * "="}+","", 0, 0, 0, 0, 1000000
print(line,head,line,sep="\n")
for i in range(7):
    amount = int(input(f"Enter amount of day {i+1} : "))
    while amount >= 1000000:
        print("Error amount")
        amount = int(input(f"Enter amount of day {i + 1} : "))
    sales = amount / 1.07
    vat = amount - sales
    ta += amount
    ts += sales
    tv += vat
    if amount > Max : Max = amount
    if amount < Min : Min = amount
    result += f"|  {i+1}  |{amount:>{len("     Amounts  ")},.2f} |{vat:>{len("    Vat(7%)   |")},.2f} |{sales:>{len("    Sales    ")},.2f} |\n"
h = "| day |     Amounts   |    Vat(7%)    |     Sales     |"
l = f"+{(len(h)-2) * "="}+"
print(f"\n{"Report Sale of Fitm shop":^{len(h)}}",l,h,l,result+l,sep="\n")
print(f"|Total|{ta:>{len("          1.00")},.2f} |{tv:>{len("           0.07")},.2f} |{ts:>{len("         0.93")},.2f} |",l,sep="\n")
print(f"Maximum Amount :    {Max:,.2f}\nMinimum Amount :    {Min:,.2f}\n")