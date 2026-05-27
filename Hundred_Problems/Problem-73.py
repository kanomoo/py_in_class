# #book class

# class Book:
#     def __init__(self, name:str, status:str):
#         self.name = name
#         self.status = status

#     def __str__(self) -> str:
#         return f"Book Name : {[self.name]}, Status : {[self.status]}"

# # book = Book("f","e.g")
# # print(book)

# while True:
#     print("Book Class\n\n1. Create a new book\n2. Display the book's information\n3. Update the book's status\n4. Exit the program\n")
#     choice = int(input("Select choice : "))
#     match choice:
#         case 1:
#             name = input("Please input name : ")
#             status = input("Please input status : ")
#             book = Book(name,status)
#         case 2:
#             try:
#                 print(book)
#             except:
#                 print("No book created yet.")
#         case 3:
#             try:
#                 status = input("Please input update book's status : ")
#                 book.status = status
#                 print("Status updated.")
#             except:
#                 print("No book to update.")
#         case 4:
#             print("Exit Program")
#             break
#         case _:
#             print("No choice")

class Book:
    def __init__(self, name: str, status: str):
        self.name, self.status = name, status
    
    def __str__(self) -> str:
        return f"Book Name:[{self.name}], Status: [{self.status}]"

def menu() -> None:
    while True:
        select = input("1. Create a new book\n2. Display the book's information\n3. Update the book's status\n4. Exit the program\nSelect: ")
        match select:
            case "1": book = Book(input("\nEnter book name: "), input("Enter status: ")); print()
            case "2": print("\n" + str(book) + "\n")
            case "3": book.status = input("\nEnter status: "); print()
            case "4": print("\nExit Program.", end = ""); exit()

if __name__ == "__main__":
    menu()