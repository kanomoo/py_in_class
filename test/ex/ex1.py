head = "| Main Menu |"
line = "=" * len(head)
while True:
    print(line,head,line," 1. Triangle 1\n 2. Triangle 2\n 3. Triangle 3\n 4. Triangle 4\n 5. Triangle 5\n 6. Exit",sep="\n")
    choice = int(input("Enter Choice : "))
    match choice:
        case 1:
            name = input("\nEnter name : ")
            print()
            for i in range(len(name)):
                print(" " * i,name[i:],name[1:len(name)-i],sep="")
        case 2:
            name = input("\nEnter name : ")
            print()
            for i in range(len(name)):
                print(" " * (len(name) - i-1),name[len(name) - i-1:],name[::-1][1:i+1],sep="")
        case 3:
            Name, name = "", input("\nEnter name : ")
            print()
            for i in name:
                Name += i
                Name += " "
            for i in range(0,len(Name),2):
                print(" " * (len(name) - (i//2)-1),Name[:i+1],sep="")
        case 4:
            Name, name = "", input("\nEnter name : ")
            print()
            for i in name:
                Name += i
                Name += " "
            for i in range(0, len(Name), 2):
                print(" " * (i//2 ),Name[:len(Name) - i],sep="")
        case 5:
            name = input("\nEnter name : ")
            print()
            for i in range(len(name)):
                print(" " * (len(name) - i - 1), name[len(name) - i - 1:], name[::-1][1:i + 1], sep="")
            for i in range(len(name)):
                print(" " * i,name[i:],name[::-1][1:len(name)-i],sep="")
        case 6:
            print("Exit Program...")
            break
    print()