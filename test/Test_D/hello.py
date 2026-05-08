# grade = int(input("Enter grade : "))
# if grade >= 80:
#     print("A")
# elif grade >= 70:
#     print("B")
# else:
#     print("D")



# num1 = int(input())
# op = input("Enter op : + - * /")
# if (op == "/"): print("ผลลัพธ์", num1  / num2)
# elif (op == "+") print("ผลลัพธ์", num1 + num2)



# num1 = 10
# num2 = 50

# print(min(num1, num2))
# print(max(num1, num2))



# str_number, output, Max, Min, total, average = "", "\n", 0, 0, 0, 0
# for i in range(1,4):
#     num = int(input(f"Enter value number{i} : "))
#     if i == 1: Min = num
#     Min, Max, total = min(Min,num), max(Max,num), float(total + num)
#     str_number += str(num) + " "
# average = f"{float(total / i):.2f}"
# output += f"Maximum value : {Max}\nMinimum value : {Min}\nAverage value : {average}\nLen of average = {len(str(average))}"
# print(str_number, output, sep="\n")


# num, Max = int(input(">> Program Find Maximum Digit<<\nEnter integer number : ")), 0
# for i in str(num): Max = max(Max,int(i))
# print(f"Maximum Digit of integer number {num} = {Max}")



# num = int(input(">> Program Find Maximum Digit<<\nEnter integer number : "))
# print(f"Maximum Digit of integer number {num} = {max(str(num))}")



# num = int(input("Enter num : "))
# for i in range(1,num + 1): print(" " * (num - i) + "*" * i)


# for i  in range(5): print("*", i)



# count = int(input("Enter number : "))
# while True:
#     if count == 0: break
#     else: count = int(input("Enter number : "))





# end = int(input("Enter number"))
# count = 0
# while count <= end:
#     count += 1
#     if count == 5: continue
#     elif count >= 10: break
#     print(count)



# name = "111111111111111111111"
# count_a = 0
# count_b = 0
# for i in name:
#     if i == "A": count_a += 1
#     elif i == "B": count_b += 1

# print(f"A = {count_a}, B = {count_b}")




# num = int(input("Enter mount: "))
# if num > 0 and num <= 12:
#     if num == 2: print(28)
#     elif (num <= 7):
#         if (num % 2 == 0): print(30)
#         else: print(31)
#     elif num >= 8:
#         if (num % 2 == 0): print(31)
#         else: print(30)
# else: print("No mount")





# while True:
#     num = int(input("Enter mount: (-1 is Exit) : "))
#     if num > 0 and num <= 12:
#         if num == 2: print("Day : 28")
#         elif (num <= 7):
#             if (num % 2 == 0): print("Day : 30")
#             else: print("Day : 31")
#         elif num >= 8:
#             if (num % 2 == 0): print("Day : 31")
#             else: print("Day : 30")
#     elif num == -1:
#         print("Exit Program.")
#         break
#     else: print("No mount")


# txt = "123456"
# for i in range(0, len(txt), 2): print(txt[i])

# for i in range((len(num) - 1),0,-1): print(num[i])



# num, num_re = input("Input : "), ""
# for i in num: num_re = i + num_re
# print("Output: ", "Palindrome" if num == num_re else "Not Palindrome", sep="")

# count = 0
# for i in range(1,101):
#     if (i % 7 == 0):
#         if count < 5:
#             print(i, end = " ")
#             count += 1
#         else: break
    



# num = 1234
# print(num % 10)
# num = num // 10
# print(num % 10)


# num, num_re = 1234, ""
# while True:
#     if num != 0:
#         num_re += str(num % 10)
#         num = num // 10
#     else:
#         print(num_re)
#         break
    
    
# num, num_re = 1234, ""
# while num != 0:
#         num_re += str(num % 10)
#         num = num // 10
# print(num_re)



# def displayName(name, score):
#     print(name + " managed to get into position " + str(calculateHighScorePosition(score)) + " on the high score list")

# def calculateHighScorePosition(score):
#     result = 0
#     if (score >= 1000): result = 1
#     elif (score >= 500): result = 2
#     elif (score >= 100): result = 3
#     else: result = 4
#     return result

# nameList, scoreList = ["Tom", "Bob", "Percy", "Gilbert", "James"], [1500, 1000, 500, 100, 25]

# for index, value in enumerate(nameList): displayName(value, scoreList[index])
# # displayName("Tom", 1500)
# # displayName("Bob", 1000)
# # displayName("Percy", 500)
# # displayName("Gilbert", 100)
# # displayName("James", 25)

# count = 0
# output = ""
# for i in range(1, 101):
#     if count <= 1:
#         output += str(i) + " "
#         count += 1
#     if count >= 2:
#         count = 0
#         print(output)
#         output = ""

# money, total, i = 0, 0, 0
# while True:
#     i += 1
#     money = int(input(f"Day {i} : "))
#     total += money
#     if total >= 1000:
#         break




# total = 0
# for i in range(1,101):
#     total += i
#     print(f"{total - i} + {i} = {total}")



# num = int(input("enter number : "))
# for i in range(1,13):
#     print(str(num) + " * " + str(i) + " = " + str(num * i))

# number = 0
# if number < 1:
#     pass
# elif number > 100:
#     pass
# else:
#     for i in range(13):

# print(f"|{"1000":>10}|")

# print(f"|{"1000".rjust(10)}|")

# print(format(1000, ",.2f").center(10))
# print(format(1000, "^10,.2f"))


# head = "+----------------------------------------+"
# Len = len(head) - 2
# money = 0
# output = head + f"\n|{"Currency Convert":^{Len}}|\n" + head + f"\n|{"0.Exit":<{Len}}|\n|{"1.Enter money":<{Len}}|\n|{"2.Convert THB to USD(33 THB / 1 USD)":<{Len}}|\n|{"3.Convert THB to JPY(0.2 THB / 1 JPy)":<{Len}}|\n|{"4.Convert THB to EUR(37 THB / 1 EUR)":<{Len}}|"
# output += "\n" + head
# output += "\nEnter choice : "
# choice = int(input(output))
# match choice:
#     case 0:
#         print("Exit Program.")
#         exit
#     case 1:
#         money = int(input("Enter money : "))
#         print(f"your money : {money:,.2f} (THB)")
#     case 2:
#         print("test")
#     case 3:
#         print("asdfasdf")


# choice = int(input("Enter choice : "))
# if choice == 1: print("test = 1")
# elif choice == 2: print("test = 2")
# else: print("No Choice")
    
    
# choice = int(input("Enter choice : "))
# match choice:
#     case 1: print("test = 1")
#     case 2: print("test = 2")
#     case _: print("No Choice")




# output = ""
# head = "+----------------------------------------+\n"
# output += head
# output += f"|{"Currency Convert":^40}|\n"
# output += head
# output += f"|{"1.Enter money":<40}|\n"
# output += f"|{"2.Enter money":<40}|\n"
# output += head
# output += "Enter choice : "
# choice = input(output)


# print(("+----------------------------------------+"))
# print(f"|{"Currency Convert":^40}|")
# print(("+----------------------------------------+"))
# print(f"|{"1.Enter money":<40}|")
# print(f"|{"2.Csdfads":<40}|")
# print(("+----------------------------------------+"))
# choice = input("Enter choice : ")