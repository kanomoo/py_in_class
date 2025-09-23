# from random import randint

# def inputSale(Sales):
#     for n in range(1,5):
#         key = input("Enter branch name : ")
#         value = []
#         for m in range(1,5):
#             data = float(input(f"Enter sales in Quarter {m} : "))
#             value.append(data)
#         Sales[key] = value

# def calTOtalSale(Sales):
#     for key in Sales:
#         Sales[key].append(sum(Sales[key]))

# def reportSale(Sales):
#     result = ("=" * 74) + "\n"
#     result += "|No.| Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |   Total  |\n"
#     n = 1
#     for key in Sales:
#         result += "|%2d | %11s |"%(n,key)
#         for sale in Sales[key]:
#             result += " %8.2f |"%(sale)
#         result += ("\n")
#         n += 1
#     result += ("=" * 74) + "\n"
#     print(result)

# Sales = {}
# inputSale(Sales)
# calTOtalSale(Sales)
# reportSale(Sales)
# for key in Sales:
#     print(key, Sales[key])

#  ================================

def input_data():
    data = {}
    for i in range(4):
        name = input("Enter branch name : ")
        sales = []
        for n in range(4):
            sale = float(input(f"Enter sales in Quater {n+1} : "))
            sales.append(sale)
        data[name] = sales
    return(data)

def report(data):
    result = ""
    head = "| No. | Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |   Total  |"
    line = "=" * len(head)
    result += f"{line}\n{head}\n{line}\n"
    n = 0
    for i in data:
        n += 1
        result += f"|  {n}  |{i:>12} |"
        data[i].append(sum(data[i]))
        for j in data[i]:
            j = int(j)
            result += f"{j:9.2f} |"
        result += "\n"
    result += line
    print(result)

def main():
    data = input_data()
    report(data)
    for i in data:
        print(i,data[i])

if __name__ == "__main__":
    main()