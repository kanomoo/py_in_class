from random import randint
def data_sales():
    sales = {}
    total = 0
    for i in range(1,16):
        total = 0
        day = []
        for n in range(7):
            day.append(randint(100,5000))
            total += day[n]
        day.append(total)
        sales[i] = day
    return sales

def total(sales):
    total = []
    total_day = []
    for day in range(8):
        for key in sales:
            total.append(sales[key][day])
        total_day.append(sum(total))
    return total_day

def report(sales,total):
    head = ": No.:   Day  1   :   Day  2   :   Day  3   :   Day  4   :   Day  5   :   Day  6   :   Day  7   :   Total     :"
    line = "-" * len(head)
    print(f"{"Report of Sales":^110}\n{line}\n{head}\n{line}")
    for i in sales:
        print(f": {i:2} :{sales[i][0]:11,.2f} :{sales[i][1]:11,.2f} :{sales[i][2]:11,.2f} :{sales[i][3]:11,.2f} :{sales[i][4]:11,.2f} :{sales[i][5]:11,.2f} :{sales[i][6]:11,.2f} :{sales[i][7]:12,.2f} :")
    print(line)
    low = "Total:"
    for i in range(8):
        if i == 7:
            low += f"{total[i]:12,.2f} :"
            break
        low += f"{total[i]:11,.2f} :"
    print(low)
    print(line)

sales = data_sales()
total = total(sales)
report(sales,total)