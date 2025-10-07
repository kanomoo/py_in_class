def enter_data():
    print("Enter data prodcut.")
    p_id = input("Input Proeduct id : ")
    p_name = input("Input prodcut name : ")
    p_price = input("Input product price : ")
    p_quantity = input("Input product quantity : ")
    with open(r"AllChapter\chapter 10\test_w4\product.txt","a",encoding="utf-8") as fin:
        fin.writelines(f"{p_id},{p_name},{p_price},{p_quantity}\n")

def report_file():
    result = ""
    n = 0
    with open(r"AllChapter\chapter 10\test_w4\product.txt") as fout:
        data = [i.strip("\n").split(",") for i in fout]
        for products in data:
            n += 1
            product = " | ".join(f"{product:>7}" for product in products)
            result += f"|Product {n:2} | {product} |\n"
    print(result+f"Total product : {n}")
    print(products)
    return data

def report_product():
    head = "| No.|  Id  |  Name     |     Price   |Quantity|    Total    |"

report_file()