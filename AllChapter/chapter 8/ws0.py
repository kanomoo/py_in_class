# def check_rate(total):
#     if total > 20000: return(0.10)
#     elif total > 10000: return(0.075)
#     elif total > 5000: return(0.05)
#     elif total > 1000: return(0.025)
#     else: return(0.0)

# def get_sale():
#     global sales
#     for n in range(1,8):
#         sale = float(input(f"Enter sale day {n} : "))
#         sales += (sale,)
    
# def sum_sale():
#     total = 0
#     for n in range(len(sales)):
#         total += sales[n]
#     return total

# def report():
#     print(f"\nTotal sale : {total_sale:.2f}")
#     print(f"Commision rate : {rate*100:.2f}%")
#     print(f"Total Commision : {commision:.2f}")

# sales = ()
# get_sale()
# total_sale = sum_sale()
# rate = check_rate(total_sale)
# commision = total_sale * rate
# report()



# def Input():
#     global sales
#     for i in range(7):
#         sale = int(input(f"Enter sale day {i+1} : "))
#         sales += (sale,)
#     return sum(sales)

# def Commission_rate(total):
#     com = {20000:10,10000:7.5,5000:5,1000:2.5,0:0}
#     for i in com: 
#         if total > i: return com[i]

# def Report():
#     print(f"\nTotal sale : {total:.2f}\nCommision rate : {rate:.2f}%\nTotal commision : {total * rate/100:.2f}")

# sales = ()
# total = Input()
# rate = Commission_rate(total)
# Report()




def Commission_rate(total):
    com = {20000:10,10000:7.5,5000:5,1000:2.5,0:0}
    for i in com: 
        if total > i: return com[i]

def Input():
    total = 0
    for i in range(7):
        sale = int(input(f"Enter ale day {i+1} : "))
        total += sale
    return total

def Report():
    print(f"\nTotal sale : {total:.2f}\nCommision rate : {rate:.2f}%\nTotal commision : {total * rate/100:.2f}")

total = Input()
rate = Commission_rate(total)
Report()