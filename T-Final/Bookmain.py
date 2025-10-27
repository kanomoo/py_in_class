from BookModule import *

def main():
    while True:
        choice = input(f"{"=" * 13}\n| Book Menu |\n{"=" * 13}\n 1. Add Book\n 2. Edit Book\n 3. Delete Book\n 4. Read file\n 5. Report Book\nSelect choice : ")
        match choice:
            case "0":
                print("Exit Program...")
                exit()
            case "1":
                add_book(r"T-Final/book.txt")
            case "2":
                edit_book(r"T-Final/book.txt")
            case "3":
                del_book(r"T-Final/book.txt")
            case "4":
                read_file(r"T-Final/book.txt") 
            case "5":
                report_book(r"T-Final/book.txt")

if __name__ == "__main__":
    main()