# name = input("Enter name : ")
# surname = input("Enter surname : ")
# age = int(input("Enter age : "))
# print(f"\nMy name is {name}\nMy surname is {surname}\nNow i'm {age} years old.\nl'll finish undergraduate in {age + 4} years old.")
from numpy.ma.extras import average

# name, surname, age = input("Enter name : "), input("Enter surname : "), int(input("Enter age : "))
# print(f"\nMy name is {name}\nMy surname is {surname}\nI'll finish undergraduate in {age + 4} years old.")


# ทำแบบบรรทัดเดียวใช้ ; จบ
# name, surname, age = input("Enter name : "), input("Enter surname : "), int(input("Enter age : "));print(f"\nMy name is {name}\nMy surname is {surname}\nI'll finish undergraduate in {age + 4} years old.")

# print((lambda name, surname, age: f"\nMy name is {name}\nMy surname is {surname}\nI'll finish undergraduate in {age + 4} years old.")(input("Enter name : "), input("Enter surname : "), int(input("Enter age : "))))

# for i in range(1,6):
#     print("*" * i)

# for i in range(5,0,-1):
#     print("*" * i)

# for i in range(1,6):
#     print("*" * i)
# for i in range(4,0,-1):
#     print("*" * i)


# for i in range(1,6):
#     print(" " * (5 - i) + "*" * i)

# num = int(input("Enter number : "))
# for i in range(1,num+1):
#     print("*" * i)

# num = int(input("Enter number : "))
# for i in range(num,0,-1):
#     print("*" * i)

# num = int(input("Enter number : "))
# for i in range(1,num+1):
#     print(" " * (num - i) + "*" * i)

# num = int(input("Enter number : "))
# for i in range(1,num+1):
#     print("*" * i)
# for i in range(num-1,0,-1):
#     print("*" * i)




# for i in range(1,6):
#     print(" " * (i - 5 ) + "*" * i)
# for i in range(4,0,-1):
#     print("*" * i)

# for i in range(1,6):
#     print("*" * i)


# height = float(input("Enter your height in cm: "))
# weight = float(input("Enter your weight in kg: "))
# print(f"Your height is {height:.2f} cm")
# print(f"Your weight is {weight:.2f} kg")


# number = int(input("Enter integer : "))
# if number % 2 == 0:
#     print(f"{number} is even number")
# else:
#     print(f"{number} is odd number")


# total = 0
# for i in range(1,6):
#     num = int(input(f"Enter integer {i} : "))
#     if num % 2 == 0:
#         print(f"{num} is even number")
#     else:
#         print(f"{num} is odd number")
#     total += num
# if total % 2 == 0:
#     print(f"Total ({total}) is even number")
# else:
#     print(f"Total ({total}) is odd number")


# num1 = int(input("Enter integer1 : "))
# num2 = int(input("Enter integer2 : "))
# choice = input("Select calculation(+ - * /) : ")
# if choice == "+":
#     print(f"result: {num1 + num2}")
# elif choice == "-":
#     print(f"result: {num1 - num2}")
# elif choice == "*":
#     print(f"result: {num1 * num2}")
# elif choice == "/":
#     if num1 == 0 or num2 == 0:
#         print("Cannot be divided by 0")
#     else:
#         print(f"result: {num1 / num2}")

# Max = 0
# print(">> Program Find Maximum Digit <<")
# num = int(input("Enter integer number: "))
# for i in str(num):
#     if int(i) >= int(Max):
#         Max = i
# print(f"Maximum Digit of integer number {num} = {Max}"


# print(">> Program Find Maximum Digit <<")
# num = int(input("Enter integer number: "))
# print(f"Maximum Digit of integer number {num} = {max(str(num))}")

# for i in range(1,13):
#     print()
#     for n in range(1,13,2):
#         print(f"{i} * {n} = {i * n}")

# for i in range(1,13):
#     print()
#     for n in range(1,13,2):
#         print(f"{i} * {n} = {i * n}")

# base = int(input("Enter the integer base value : "))
# exp = int(input("Enter the integer exp value : "))
# print(f"exponent of {base} ^ {exp} = {pow(base,exp)}")
# base_float = float(input("\nEnter the decimal number base value : "))
# exp_float= float(input("Enter the decimal power value : "))
# print(f"exponent of {base_float} ^ {exp_float} = {base_float ** exp_float} -> {base_float ** exp_float:.2f}")

# num1 = int(input("Enter value number1 : "))
# num2 = int(input("Enter value number2 : "))
# num3 = int(input("Enter value number3 : "))
# print(f"Your enter number : {num1} {num2} {num3}")
# print(f"\nMaximum value : {max(num1,num2,num3)}")
# print(f"Minimum value : {min(num1,num2,num3)}")
# print(f"Average value : {(num1+num2+num3) / 3:.2f}")
# print("Len of average = ",len(f"{(num1+num2+num3) / 3:.2f}"))
