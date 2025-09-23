# library book class with a menu interface

class LibraryBook:
    def __init__(self, title: str, author: str, year_published: int, isbn: str):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.isbn = isbn
        self.status = "available"

    def check_out(self):
        self.status = "check out"

    def return_book(self):
        self.status = "available"

    def display_into(self):
        print(f"Title {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}\n"
              f"ISBN: {self.isbn}\nStatus: {self.status}")

library = [] # จะแสดงว่าเป็น list ที่เก็บ object อยู่

while True:
    print("\nLibrary\n\n1. Add a new book\n2. Check out a book\n3. Return a book\n4. Display information about a specific book\n"
          "5. Display all books in the library\n6. Exit\n")
    choice = int(input("Please select choice : "))
    match choice:
        case 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter year: "))
            isbn = input("Enter isbn: ")
            book = LibraryBook(title,author,year,isbn)
            library.append(book) # list สามารถเก็บ object ของ class librarybook ได้ และเรียนใช้ผ่าน for
        case 2:
            num = input("\nPlease Enter isbn to check out : ")
            for i in library:
                if i.isbn == num and i.status == "available":
                    i.check_out()
                    print(f"{i.isbn} check out.")
                elif num not in library:
                    print(f"{num} is not in library")
                elif i.status == "check out":
                    print(f"{num} not check out ")
        case 3:
            num = input("\nPlease Enter isbn to return a book : ")
            for i in library:
                if i.isbn == num and i.status == "check out":
                    i.return_book()
                    print(f"{i.isbn} return.")
                elif num not in library:
                    print(f"{num} is not in library")
                elif i.status == "available":
                    print(f"{num} not check out ")
        case 4:
            num = input("\nPlease Enter isbn : ")
            for i in library:
                if i.isbn == num:
                    i.display_into()
        case 5:
            print()
            for i in library:
                i.display_into()
                print("=" * 20)
        case 6:
            print("Exit Program.")
            break



# from datetime import datetime
#
# class LibraryBook:
#     def __init__(self, title: str, author: str, year_published: int, isbn: str):
#         self.title = title
#         self.author = author
#         self.year_published = year_published
#         self.isbn = isbn
#         self.status = "available"
#
#     def check_out(self):
#         if self.status == "available":
#             self.status = "checked out"
#             print(f"'{self.title}' has been checked out.")
#         else:
#             print(f"'{self.title}' is already checked out.")
#
#     def return_book(self):
#         if self.status == "checked out":
#             self.status = "available"
#             print(f"'{self.title}' has been returned.")
#         else:
#             print(f"'{self.title}' is already available.")
#
#     def display_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Year Published: {self.year_published}")
#         print(f"ISBN: {self.isbn}")
#         print(f"Status: {self.status}")
#
#
# def valid_year(year_str):
#     if year_str.isdigit():
#         year = int(year_str)
#         return year > 0 and year <= datetime.now().year
#     return False
#
#
# def valid_isbn(isbn):
#     return isbn.isdigit() and len(isbn) in (10, 13)
#
#
# def get_non_empty_string(prompt):
#     while True:
#         value = input(prompt).strip()
#         if value:
#             return value
#         print("Input cannot be empty.")
#
#
# def get_valid_year():
#     while True:
#         year_input = input("Enter year published: ")
#         if valid_year(year_input):
#             return int(year_input)
#         print("Invalid year. Please enter a valid year.")
#
#
# def get_valid_isbn():
#     while True:
#         isbn = input("Enter ISBN (10 or 13 digits): ")
#         if valid_isbn(isbn):
#             return isbn
#         print("Invalid ISBN. Must be 10 or 13 digits and numeric.")
#
#
# def main():
#     library = []
#
#     while True:
#         print("\nLibrary Menu")
#         print("1. Add a new book")
#         print("2. Check out a book")
#         print("3. Return a book")
#         print("4. Display information about a specific book")
#         print("5. Display all books in the library")
#         print("6. Exit")
#
#         choice = input("Select an option (1-6): ")
#
#         if choice == "1":
#             title = get_non_empty_string("Enter book title: ")
#             author = get_non_empty_string("Enter book author: ")
#             year = get_valid_year()
#             isbn = get_valid_isbn()
#             book = LibraryBook(title, author, year, isbn)
#             library.append(book)
#             print("Book added successfully.")
#
#         elif choice == "2":
#             isbn = input("Enter ISBN of book to check out: ")
#             for book in library:
#                 if book.isbn == isbn:
#                     book.check_out()
#                     break
#             else:
#                 print("Book not found.")
#
#         elif choice == "3":
#             isbn = input("Enter ISBN of book to return: ")
#             for book in library:
#                 if book.isbn == isbn:
#                     book.return_book()
#                     break
#             else:
#                 print("Book not found.")
#
#         elif choice == "4":
#             isbn = input("Enter ISBN of book to display: ")
#             for book in library:
#                 if book.isbn == isbn:
#                     book.display_info()
#                     break
#             else:
#                 print("Book not found.")
#
#         elif choice == "5":
#             if library:
#                 for book in library:
#                     book.display_info()
#                     print("-" * 40)
#             else:
#                 print("No books in library.")
#
#         elif choice == "6":
#             print("Exiting program.")
#             break
#
#         else:
#             print("Invalid choice. Please select between 1 and 6.")
#
#
# if __name__ == "__main__":
#     main()
