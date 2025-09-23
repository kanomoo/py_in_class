# แบบทำเอง ###########################################################################
# def add_product():
#     print("Enter data product.")
#     p_id = input("Input product id : ")
#     p_name = input("Input name : ")
#     p_price = input("Input price : ")
#     p_quantity = input("Input quantity : ")
#     fout = open("product.txt","a",encoding="UTF-8")
#     fout.write(p_id + "," + p_name + "," + p_price + "," + p_quantity + "\n")
#     fout.close()
#     print("Save Data Product allready.")
#
# def report_from_file():
#     with open("product.txt") as fin:
#         n = 1
#         data = []
#         for i in fin:
#             i = i.rstrip("\n")
#             data.append(i.split(","))
#         for i in data:
#             print(f"Product {n:2} :{i[0]:6}:{i[1]:5}:{i[2]:5}:{i[3]:5}")
#             n += 1
#         print(f"Total product : {n-1}")
#     return data
#
# def report(data):
#     head = "| No.|  Id  |  Name     |     Price   |Quantity|    Total    |"
#     line = "-" * len(head)
#     print(format("Report Product","^63"))
#     print(line,head,line,sep="\n")
#     n = 1
#     for i in data:
#         print(f"|{n:3} |{i[0]:5} |{i[1]:<11}|{float(i[2]):12,.2f} |{float(i[3]):7.2f} |{int(i[2]) * int(i[3]):12,.2f} |")
#         n += 1
#     print(line)
#
# # add_product()
# # data = report_from_file()
# # report(data)

# แบบทำเองผสมสายชม ###########################################################################

# def add_product(filename):
#     print("Enter data product.")
#     prod_id = input("Input product id : ")
#     prod_name = input("Input product name : ")
#     prod_price = input("Input product price : ")
#     prod_qty = input("Input product quantity : ")
#     try:
#         fout = open(filename,"a",encoding="UTF-8")
#         fout.write(prod_id + "," + prod_name + "," + prod_price + "," + prod_qty + "\n")
#         fout.close()
#     except FileNotFoundError: # หากเกิดข้อผิดพลาดว่าไม่พบไฟล์
#         print(f"{filename} is not found")
#     else:
#         print("Save Data Product allready.\n")
#
# def report_from_file(filename):
#     n = 0
#     try:
#         with open(filename,encoding="UTF-8") as fin:
#             for prod in fin:
#                 n += 1
#                 prod_list = prod.rstrip("\n").split(",")
#                 product = ":".join(f"{data:>5}" for data in prod_list)
#                 print(f"Product {n:2} : " + product + ":")
#             print(f"Total Product {n:2}\n")
#     except FileNotFoundError:# หากเกิดข้อผิดพลาดว่าไม่พบไฟล์
#         print(f"{filename} is not found")
#
# def read_product(filename):
#     products = []
#     try:
#         with open(filename,encoding="UTF-8") as fin:
#             for prod in fin:
#                 prod = prod.rstrip("\n").split(",")
#                 products.append(prod)
#     except FileNotFoundError:
#         print(f"{filename} is not found")
#     else:
#         return products
#
# def report_product(products):
#     head = "| No.|  Id  |  Name     |     Price   |Quantity|    Total    |\n"
#     line = "-" * (len(head)-1) + "\n"
#     head2 = (format("Report Product","^62")) + "\n"
#     n = 1
#     mess = ""
#     try:
#         for i in products:
#             price = float(i[2])
#             qty = float(i[3])
#             total = price * qty
#             mess += f"|{n:3} |{i[0]:5} |{i[1]:10} |"
#             mess += f"{price:>11,.2f} |{float(i[3]):>7,} |"
#             mess += f"{total:>13,.2f} |\n"
#             n += 1
#     except IndexError:
#         print("Index list not found.")
#     else:
#         print(head2,line,head,line,mess,line,sep="")
#
# def main():
#     head = "| Product  Menu |"
#     line = "=" * len(head)
#     while True:
#         print(line,head,line,sep="\n")
#         filename = "product.txt"
#         choice = input("1. Add Product\n2. Report Product from File\n3. Report Product by Price\n4. Exit\nEnter Choice : ")
#         match choice:
#             case "1":
#                 add_product(filename)
#             case "2":
#                 report_from_file(filename)
#             case "3":
#                 products = read_product(filename)
#                 report_product(products)
#             case "4":
#                 print("Exit")
#                 break
#             case _:
#                 print("No choice")
#
# if __name__ == "__main__":
#     main()

# ทำเองรอบ 2
def add_product(filename):
    print("Enter data product.")
    p_id = input("Input Product id : ")
    p_name = input("Input Product name : ")
    p_price = input("Input Product price : ")
    p_q = input("Input Product quantity : ")
    try:
        fout = open(filename,"a",encoding="UTF-8")
        fout.write(p_id + "," + p_name + "," + p_price + "," + p_q + "\n")
        fout.close()
    except FileNotFoundError:
        print(f"{filename} is not found")
    else:
        print("Save Data Product allready.\n")

def report_from_file(filename):
    n = 0
    try:
        with open(filename) as fin:
            for data in fin:
                n += 1
                data = data.rstrip("\n").split(",")
                p = ":".join(f"{i:>5}" for i in data)
                print(f"Product {n:2} :{p}:")
            print(f"Total product : {n:2}\n")
    except FileNotFoundError:
        print(f"{filename} is not found")

def report_price(filename):
    data = []
    try:
        with open(filename) as fin:
            for i in fin:
                i = i.rstrip("\n").split(",")
                data.append(i)
            head = "| No.|  Id  |  Name     |     Price   |Quantity|    Total    |\n"
            line = "-" * (len(head)-1) + "\n"
            n = 0
            mess = ""
            for i in data:
                n += 1
                mess += f"|{n:3} |{i[0]:5} |{i[1]:10} |{float(i[2]):12,.2f} |{float(i[3]):7} |{int(i[2]) * int(i[3]):12,.2f} |\n"
    except IndexError:
        print("Index list not found.")
    else:
        print(format("Report Product","^61"))
        print(line,head,line,mess,line,sep="")

def main():
    filename = "product.txt"
    head = "| Product  Menu |"
    line = "=" * len(head)
    while True:
        print(line,head,line,sep="\n")
        mess = "1. Add Product\n2. Report Product from File\n3. Report Product by Price\n4. Exit\nEnter choice : "
        choice = input(mess)
        match choice:
            case "1":
                add_product(filename)
            case "2":
                report_from_file(filename)
            case "3":
                report_price(filename)
            case "4":
                print("Exit Program")
                break
            case _:
                print("No choice\n")

if __name__ == "__main__":
    main()