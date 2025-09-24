num = int(input("Enter number money withdraw : "))
bt = num // 1000
bf = num % 1000 // 500
bh = num % 500 // 100
print(bt,bf,bh,sep="\n")