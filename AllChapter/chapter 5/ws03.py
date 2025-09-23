# num1 = int(input("Etner number 1 : "))
# num2 = int(input("Enter number 2 : "))
# num3 = int(input("Enter number 3 : "))
# if num1 > num2:
#     if num1 > num3:
#         Max = num1
#     else:
#         Max = num3
# else:
#     if num2 > num3:
#         Max = num2
#     else:
#         Max = num3
# print("Maximum number : ", Max)

Max = 0
for i in range(3):
    num = int(input(f"Enter number {i+1} : "))
    if num > Max : Max = num
print(f"\nMaximum number : {Max}")