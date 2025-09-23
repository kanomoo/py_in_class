#นายปภาวิน ธิติชุณหกุล 6806021612037
num = float(input("Enter net price product : "))
price = num / 1.07
vat = num - price
print("Price Product :", round(price, 2))
print("Vat product :", round(vat, 2))

# product = float(input("ราคา : "))
# vat = product * 7 // 100
# buy = product - vat
# print(buy)
# print(vat)