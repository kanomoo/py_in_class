from TT2.ProductModule import *

def main():
    while True:
        choice = input(f"{"=" * 17}\n| Product  Menu |\n{"=" * 17}\n1. Add product\n2. Report Product from File\n3. Report Product by Price\n4. Edit Product\n5. Del Product\n6. Exit\nEnter Choice : ")
        match choice:
            case "1":
                add_product(r"Tutoring/TT2/product.txt")
            case "2":
                report_from_file(r"Tutoring/TT2/product.txt")
            case "3":
                report_by_price(r"Tutoring/TT2/product.txt")
            case "4":
                edit_product(r"Tutoring/TT2/product.txt")
            case "5":
                del_product(r"Tutoring/TT2/product.txt")
            case "6":
                print("\nExit Program...")
                exit()
        print()

if __name__ == "__main__":
    main()