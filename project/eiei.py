# product = int(input("ราคา : "))
# vat = product * (7 /107)
# buy = product - vat

# print ("ราคา",buy,'\nภาษีมูลค่าเพิ่ม',vat)
amount= float(input("Enter amount : "))
rate = float(input("Enter rate : "))
year = float(input("Enter Year : "))

totalrate = amount * (1+rate/100) ** year

print ("future Value = ",totalrate)
