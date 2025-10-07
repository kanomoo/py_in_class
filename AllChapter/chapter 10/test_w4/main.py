def main():
    head = "| prodcut  Menu |"
    line = "=" * len(head)
    result = f"{line}\n{head}\n{line}\n1. Add Product\n2. Report Product from File\n3. Report Prodcut by Price\n4. Exit"
    choice = input("Enter Choice : ")
    match choice:
        case "1":
            enter_data()