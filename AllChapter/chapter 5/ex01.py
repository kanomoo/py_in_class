# print(">> Program Find Maximum Digit <<")
# num = None
# while num != 0:
#     num = int(input("Enter integer number(0-exit) : "))
#     print(f"Maximum Digit of integer number {num} = {max(str(num))}") if num != 0 else print("Exit Program")


# print(">> Program Find Maximum Digit <<")
# num = None
# while num != 0:
#     num,Max = input("Enter integer number(0-exit) : "), 0
#     for i in num: 
#         if int(i) >= int(Max): Max = i
#     if num != 0: print(f"Maximum Digit of integer number {num} = {Max}") 
#     else: print("Exit Program")


print(">> Program Find Maximum Digit <<")
while True:
    num,Max = int(input("Enter integer number(0 - exit) : ")), 0
    if num == 0: break
    else:
        Max = 0
        while num > 0:
            digit = num % 10 
            num = num // 10
            if digit > Max: Max = digit
        print(f"Maximum digit : {Max}")
print("Exit Program")