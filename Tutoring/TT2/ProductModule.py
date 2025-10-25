def add_product(file):
    id = (input("Enter data product.\nInput product id : "))
    name = input("Input product name : ")
    price = (input("Input product price : "))
    quantity = (input("Input Product quantity : "))
    with open(file,"a",encoding="utf-8") as fin:
        fin.write(",".join((id,name,price,quantity))+"\n")

def report_from_file(file):
    with open(file,"r",encoding="utf-8") as fout:
        n = 0
        for i in fout:
            n += 1
            print(f"Product {n} :",":".join([f"{j:>5}" for j in i.strip("\n").split(",")]))
        print(f"Total product :  {n}")

def report_by_price(file):
    data = []
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))
    head = "| No.|  Id  |  Name     |     Price   |Quantity|     Total    |"
    line = "=" * len(head)
    result = f"{line}\n{head}\n{line}\n"
    for i,v in enumerate(data):
        result += f"| {i+1:2} |{v[0]:5} |{v[1]:10} |{int(v[2]):>12.2f} |{int(v[3]):7.1f} |{int(v[2]) * int(v[3]):13,.2f} |\n"
    result += line
    print(result)

def edit_product(file):
    data = []
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))
    id = input("Input product id : ")
    for i,v in enumerate(data):
        if id in data[i][0]:
            name = input("Input product name : ")
            price = (input("Input product price : "))
            quantity = (input("Input Product quantity : "))
            data[i] = id,name,price,quantity
            break
    with open(file,"w",encoding="utf-8") as fin:
        for i in data:
            fin.write(",".join(i)+"\n")

def del_product(file):
    data = []
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))
    id = input("Input product id : ")
    for i,v in enumerate(data):
        if id in data[i][0]:
            del data[i]
    with open(file,"w",encoding="utf-8") as fin:
        for i in data:
            fin.write(",".join(i)+"\n")