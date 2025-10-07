from ModuleProduct import *
def main():
    PRODUCTIFILE = "AllChapter/chapter 10/ws4/product.txt"
    menu = ("="*17)+"\n| Product  Menu |\n" + ("=" * 17)
    menu += "\n1. Add Product\n2. Report Product from File\n"
    menu += "3. Report Prodcut by Pridce\n4. Exit\nEnter Cohice : "
    while True:
        choice = input(menu)
        if choice == "1": add_product(PRODUCTIFILE)
        elif choice == "2": report_from_file(PRODUCTIFILE)
        elif choice == "3":
            prodcts = read_product(PRODUCTIFILE)
            report_product(prodcts)
        elif choice == "4": break
        else: print("No choice, input again.")
    print("Exit Program")

if __name__ == "__main__":
    main()