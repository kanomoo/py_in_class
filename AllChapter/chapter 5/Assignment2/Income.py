#นายปภาวิน ธิติชุณหกุล 6806021612037
income = 0
while True:
    income = int(input("Enter your income( -1 to exit) : "))
    if income == -1: break
    if income >= 0 and income <= 150000: tax = 0
    elif income >= 150001 and income <= 300000: tax = 2.5 # ต้องเอา tax ไป หาร 100 ต่อ
    elif income >= 300001 and income <= 500000: tax = 4.0
    elif income >= 500001 and income <= 800000: tax = 5.5
    elif income >= 800001 and income <= 1000000: tax = 7.5
    elif income > 1000000: tax = 10.0
    print(f"Net Income : {income:,.2f}\nTax Rate(%) : {tax:.2f}%\nAmount Tax : {income * (tax/100):,.2f}")
    print()
print("Exit Program. . .")

