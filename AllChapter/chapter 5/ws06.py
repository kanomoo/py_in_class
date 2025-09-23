Num = int(input("Enter max number : "))
for n in range(1,Num+1):
    if n % 2 == 0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")