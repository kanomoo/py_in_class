# from ModuleProduct import *
#
# head = "| Product  Menu |"
# line = "=" * len(head)
# while True:
#     print()
#     print(line,head,line,sep="\n")
#     menu = "1. Add Product\n2. Report Product from File\n3. Report Product by Price\n4. Exit\nEnter Choice : "
#     choice = input(menu)
#     match choice:
#         case "1":
#             add_product()
#         case "2":
#             data = report_from_file()
#         case "3":
#             report(data)
#         case "4":
#             print("Exit Program")
#             break
#         case _:
#             print("No choice")