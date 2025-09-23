menuStr = ("=" * 13) +"\n| Main Menu |\n" +("=" * 13) +"\n"
menuStr += """ 1. Triangle 1
 2. Triangle 2
 3. Triangle 3
 4. Triangle 4
 5. Exit
Enter Choice : """
while True:
    choice = input(menuStr)
    if choice == "1":
        num = int(input("\nEnter number of character : "))
        # for row in range(1,num+1): # outer loop
        #     for col in range(1,num+1): # inner loop
        #         if col <= row : print("*",end="")
        #         else: print(" ", end="")
        #     print()

        for row in range(1,num+1): # outer loop
            for col in range(1,row+1): #inner looop
                print("*",end="")
            print()
       
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        break
    else: print("\nInput error choice.")
print("\nExit Program...")



# head = "| Main  Menu |"
# line = len(head) * "="
# while True:
#     print(line,head,line," 1. Triangle 1\n 2. Triangle 2\n 3. Triangle 3\n 4. Triangle 4\n 5. Exit\n",sep="\n")
#     chioce = int(input("Enter Choice : "))
#     match chioce:
#         case 1:
#             num = int(input("\nEnter number of  character : "))
#             print()
#             for i in range(num):
#                 print("*" * (i+1))
#         case 2:
#             num = int(input("\nEnter number of  character : "))
#             print()
#             for i in range(num):
#                 print("*" * (num - i))
#         case 3:
#             num = int(input("\nEnter number of  character : "))
#             print()
#             for i in range(num):
#                 print(" " * (num - i),"*" * (i+1),sep="")
#         case 4:
#             num = int(input("\nEnter number of  character : "))
#             print()
#             for i in range(num):
#                 print(" " * i,"*" * (num - i),sep="")
#         case 5:
#             print("\bExit Program ...")
#             break
#         case _:
#             print("\nInput error choice.")
#     print()
        
    