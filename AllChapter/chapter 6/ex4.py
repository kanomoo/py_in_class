from random import randint
head = "Main  Menu"
line = len(head) * "="
while True:
    print(line,head,line," 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Exit",sep="\n")
    choice = int(input("Enter hoice : "))
    match choice:
        case 1: 
            num = int(input("Enter number of score : "))
        case 2:
            print("\nStart Random Scoer ...\nCheck Grade ... \n")
            h = "|Grade| Total|"
            l = len(h) * "-"
            print(l,h,l,sep="\n")
            a, b, c, d, f = 0, 0, 0, 0, 0
            for i in range(num):
                score = randint(40,90)
                if score >= 80: a += 1
                elif score >= 70: b += 1
                elif score >= 60: c += 1
                elif score >= 50: d += 1
                elif score >=  0: f += 1
            print(f"|  A  |  {a:3} |\n|  B  |  {b:3} |\n|  C  |  {c:3} |\n|  D  |  {d:3} |\n|  F  |  {f:3} |",l,f"|Total|  {num:3} |",l,sep="\n")

        case 3:
            print("Exit Program")
            break
        case _:
            print("Choice not correct.")
    print()