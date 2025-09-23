#นายปภาวิน ธิติชุณหกุล 6806021612037
amount = int(input("Enter amount : "))
rate = float(input("Enter rate : "))
year = int(input("Enter year : "))
fv = amount * ((1+(rate/100)) ** year)
print("Future value = ", fv)