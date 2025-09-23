#นายปภาวิน ธิติชุณหกุล 6806021612037
while True:
    line = "=" * 23
    print(line,"::     Main Menu     ::",line," A. Get Integer Number\n B. Summation of Digit\n C. Count Digit\n D. Exit",sep="\n")
    choice,total = input("Enter Choice : "), 0
    match choice:
        case "a" | "A":
            num = input("\nEnter long number :  ")
        case "b" | "B":
            odd, even = 0, 0
            try:
                for i in num:
                    total += int(i) #ต้องแปลง str(i) เป็น int(i)
                    if int(i) % 2 == 0: even += int(i)
                    else: odd += int(i)
            except: print("Not number")
            else: print(f"Your enter number : {num}\nSummation of digit : {total}\nSummation Odd of digit : {odd}\nSummation Even of digit : {even}")
        case "c" | "C":
            print(f"You enter number : {num}\nThis number has {max(num)} digits.")
        case "d" | "D":
            print("\nExit Program...")
            break
    print()