# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# num3 = int(input("Enter number 3 : "))
# num4 = int(input("Enter number 4 : "))
# Max = 0
# if Max < num1:
#      Max = num1
# if Max < num2:
#     Max = num2
# if Max < num3:
#     Max = num3
# if Max < num4:
#     Max = num4
# print("\nMaximum number value", Max)

Max = 0
for i in range(4):
    num = int(input(f"Enter number {i+1} : "))
    if num > Max : Max = num
print(f"\nMaximum number value {Max}")