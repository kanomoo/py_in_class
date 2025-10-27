def add_book(filename):
    data = []
    with open(filename,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))
    print(f"< Add Book >\n\nnow {len(data)} book in data.")
    id = input("Enter id  : ")
    c_id = [i for i in data[0]]
    if id not in c_id:
            name = input("Enter name : ")
            price = input("Enter price : ")
            qty = input("Enter qty : ")
    else : print("id in data not add again.")
    confirm = input("\nconfirm (Y/N) : ").lower()
    if confirm == "y": 
        with open(filename,"a",encoding="utf-8") as fin:
            fin.write(",".join((id,name,price,qty))+"\n")
    else : pass
    
def edit_book(filenamev):
    pass

def del_book(filename):
    pass

def read_file(filename):
    pass

def report_book(filename):
    pass

add_book(r"T-Final/book.txt")