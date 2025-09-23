from random import randint
line = "=" * 26
while True:
    print(line,f"{"Main Menu":^{len(line)}}",line," 1. Input number of subject (8)\n 2. Start Random Grade\n 3. Exit Program",line,sep="\n")
    choice, tc, tp = int(input("Select your Choice : ")), 0, 0
    match choice:
        case 1:
            num = int(input("Enter your number of subject : "))
            print("Press any key to continue . . . ")
        case 2:
            print("Start Random Score&Grade . . . .",line,sep="\n")
            for i in range(num):
                rd = randint(40,90)
                if rd >= 80 and rd <= 90: grade, point = "A", 4 * 3
                elif rd >= 70 and rd <80: grade, point = "B", 3 * 3
                elif rd >= 60 and rd < 70: grade, point = "C", 2 * 3
                elif rd >= 50 and rd < 60: grade, point = "D", 1 * 3
                elif rd >= 40 and rd < 500: grade, point = "F", 0 * 3
                tc += 3
                tp += point
                print(f"Your #{i+1} subject is {grade}")
            print(f"\nYour Total GPA is : {tp / tc:.2f}",line,"Press any key to continue . . . ",sep="\n")
        case 3:
            print("Exit Program . . .")
    print()