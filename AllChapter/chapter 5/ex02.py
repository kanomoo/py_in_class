# print(">> Program Find Maximum Value <<")
# num = int(input("Enter number of value(>= 1) : "))
# result, m = "", 0
# if num >= 1:
#     print(f"\nProgram get value {num} numbers.")
#     for i in range(num):
#         value = int(input(f"Enter value Number #{i+1} : "))
#         result += f" {value}," if i < num-1 else f" {value}"
#         if value > m: m = value
#     print(f"Your enter number : {result}\nMaximum value number is {m}")
# else: print("Value input not correct.")
# print("Exit Program")


print(">> Program Find Maximum Value << ")
value,result,Max = int(input("Enter number f value (>= 1 ) : ")), "Your enter number :", 0 
print(f"\nProgram get value {value} numbers.")
if value >= 1:
    for i in range(value):
        num = int(input(f"Enter value Number #{i+1} : "))
        if i < value - 1: result += f" {num},"
        else: result += f" {num}"
        if num > Max: Max = num
    print(result)
    print(f"Maximum value number is {Max}")
else: print("Value input not correct.\nExit Program")
print("Exit Program")