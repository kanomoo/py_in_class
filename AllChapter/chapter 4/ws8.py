price = 12_345.00
qty = int(input("Enter quantity product : "))

total = price * qty
print("\nTotal price : ", format(total, ",.2f"))
vat = total * 0.07
print("Vat (7%) : ", format(vat, ",.2f"))
allTotal = total + vat
print("All total : ", format(allTotal, ",.2f"))
print("All total : ", format(allTotal, "#>20,.2f"))