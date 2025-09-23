while True:
    head = "| Main  Menu |"
    line = "=" * len(head)
    print(line,head,line," 1. Triangle 1\n 2. Triangle 2\n 3. Triangle 3\n 4. Triangle 4\n 5. Triangle 5\n 6. Exit",sep="\n")
    choice = int(input("Enter Choice : "))
    match choice:
        case 1:
            # name,re = input("\nEnter name : "), ""
            name,re = "somchai", ""
            print()
            for i in range(len(name)-1,-1,-1):
                re += name[i]
            for i in range(len(name)):
                print(" " * i,end="")
                for n in range(i,len(name)):
                    print(name[n],end="")
                for r in range(1,len(name)-i):
                    print(re[r],end="")
                print()
        case 2:
            name, re = "somchai", ""
            print()
            for i in range(len(name) - 1, -1, -1):
                re += name[i]
            for i in range(len(name)):
                print(" " * (len(name) - i-1),end="")
                for n in range(i,-1,-1):
                    print(re[n],end="")
                for r in range(1,i+1):
                    print(re[r],end="")
                print()
        case 3:
            Name, re, name, l = "somchai", "", "" , 0
            print()
            for i in Name:
                name += i
                name += " "
            for i in range(len(Name)):
                l += 2
                print(" " * (len(Name) - i-1),end="")
                for i in range(0,l):
                    print(name[i],end="")
                print()
        case 4:
            Name, re, name, l = "somchai", "", "", 0
            print()
            for i in Name:
                name += i
                name += " "
            for i in range(len(Name)):
                l += 2
                print(" " * i, end="")
                for i in range(0, len(name)-l+1):
                    print(name[i],end="")
                print()
        case 5:
            name, re = "somchai", ""
            print()
            for i in range(len(name) - 1, -1, -1):
                re += name[i]
            for i in range(len(name)):
                print(" " * (len(name) - i - 1), end="")
                for n in range(i, -1, -1):
                    print(re[n], end="")
                for r in range(1, i + 1):
                    print(re[r], end="")
                print()
            for i in range(len(name)):
                print(" " * i, end="")
                for n in range(i, len(name)):
                    print(name[n], end="")
                for r in range(1, len(name) - i):
                    print(re[r], end="")
                print()
    print()