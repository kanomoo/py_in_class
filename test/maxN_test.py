print(">> Progarm Find Maximum Value <<")
value, p, m = int(input("Enter number of value (>= 1) : ")), "Your enter number : ", 0
if value >= 1 :
    print(f"Program get value {value} numbers.")
    for i in range(value):
        num = int(input(f"Enter value number {i+1} : "))
        p += f" {num}," if i < value-1 else f" {num}"
        if num > m: m = num
    print(p,f"Maximum value number is {m}",sep="\n")
else: print("Value input not correct.")
print("Exit Program")


