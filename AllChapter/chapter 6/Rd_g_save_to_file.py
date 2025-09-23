import os 
from random import randint
head = "Main  Menu"
line = len(head) * "="
num = None
while True:
    print(line,head,line," 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Show all random\n 4. Exit",sep="\n")
    choice = int(input("Enter choice : "))
    match choice:
        case 1: 
            num = int(input("Enter number of score : "))
        case 2:
            if num == None: num = int(input("Enter number of score : "))
            a, b, c, d, f = 0, 0, 0, 0, 0
            for i in range(num):
                score = randint(40,90)
                if score >= 80: a += 1
                elif score >= 70: b += 1
                elif score >= 60: c += 1
                elif score >= 50: d += 1
                elif score >=  0: f += 1
            print("\nStart Random Scoer ...\nCheck Grade ... \n")
            h = "|Grade| Total|"
            l = len(h) * "-"
            print(l,h,l,sep="\n")
            print(f"|  A  |  {a:3} |\n|  B  |  {b:3} |\n|  C  |  {c:3} |\n|  D  |  {d:3} |\n|  F  |  {f:3} |",l,f"|Total|  {num:3} |",l,sep="\n")

            file = "AllChapter\chapter 6\ test.txt"
            with open(file,"a") as fount:
                h1 = "| A | B | C | D | F |"
                l1 = len(h1) * "-"
                fount.write(f"{h1}\n|{a:3}|{b:3}|{c:3}|{d:3}|{f:3}|\n{l1}\n")

        case 3:
            show_total = []
            file = "AllChapter\chapter 6\ test.txt"
            with open(file) as fin:
                while True:
                    t = (fin.readline())
                    t = t.replace("|","")
                    t = t.strip()
                    t = t.split()
                    if t == []: break
                    if t[0] >= "0" and t[0] != "A": show_total.append(t)            
                    
                    
            print(f"\n{"+" + ("=" * 40) + "+"}")
            for i in range(len(show_total)):
                total = 0
                for n in range(len(show_total[i])):
                    total += int(show_total[i][n])
                print(f"| {i+1:2} | {show_total[i][0]:>3} | {show_total[i][1]:>3} | {show_total[i][2]:>3} | {show_total[i][3]:>3} | {show_total[i][4]:>3} | {total:>3} |")
            print(f"{"+" + ("=" * 40) + "+"}")
        case 4:
            print("Exit Program")
            break
        case _:
            print("Choice not correct.")
    input("\nPlease enter to continue...")
    os.system("cls")
    print()