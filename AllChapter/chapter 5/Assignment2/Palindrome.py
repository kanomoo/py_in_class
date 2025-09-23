#นายปภาวิน ธิติชุณหกุล 6806021612037
print(">> Program Palindrome Number <<")
num = input("Enter integer number : ")
for i in range(len(num) // 2): # หารตัดเศษ 2 เพื่อหา palindrome ง่ายๆ
    if num[i] == num[len(num)-1 - i]: #num[len(num)-1 - i] หาค่าตัวด้านหลัง
        result = "Palindrome"
        print(f"Digit {num[i]} equal to Digit {num[len(num)-1 - i]}")
    else:
        result = "not Palindrome"
        print(f"Digit {num[i]} not equal to Digit {num[len(num)-1 - i]}")
        break
print(f"Your enter number : {num} is {result} Number.\nExit Program")