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



num = int(input("Enter num : "))
for i in range(1,num + 1): print(" " * (num - i) + "*" * i)

