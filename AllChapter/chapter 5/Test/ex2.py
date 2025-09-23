head = ": Porgram Cal Vat :"
line, result, ta, tv, ts = len(head) * "=", "", 0, 0, 0
print(line,head,line,sep="\n")
for i in range(7):
    amount = int(input(f"Enter amount of day {i+1} : "))
    while amount >= 1000000:
        print("Please input amount range (1-1000000)")
        amount = int(input(f"Enter amount of day {i+1} : "))
    if i == 0: Max = Min = amount
    else:
        Max = max(Max,amount)
        Min = min(Min,amount)
    sales = amount / 1.07 ; vat = amount - sales ; ta += amount ; tv += vat ;ts += sales
    result += f"|  {i+1}  |{amount:>14,.2f} |{vat:14,.2f} |{sales:14,.2f} |\n"
h = "| day |     Amounts   |    Vat(7%)    |     Sales     |"
l = f"+{(len(h)-2) * "="}+"
print(f"\n{"Report Sale of Fitm Shop":^{len(h)}}",l,h,l,result+l,sep="\n")
print(f"|Total|{ta:>14,.2f} |{tv:14,.2f} |{ts:14,.2f} |",l,sep="\n")
print(f"Maximum Amount :    {Max:,.2f}\nMinimum Amount :    {Min:,.2f}\n")
print() #เดี๋ยวมันไม่ 20 บรรทัด เลข 19 ไม่สวยๆ