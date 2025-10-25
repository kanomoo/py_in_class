from BookModule import *

def main():
    while True:
        choice = input(f"{"=" * 13}\n| Book Menu |\n{"=" * 13}\n 1. Add Book\n 2. Edit Book\n 3. Delete Book\n 4. Read file\n 5. Report Book\nSelect choice : ")
        match choice:
            case "0":
                print("Exit Program...")
                exit()
            case "1":
                add_book()
            case "2":
                edit_book()
            case "3":
                del_book()
            case "4":
                read_file() 
            case "5":
                report_book()

if __name__ == "__main__":
    main()