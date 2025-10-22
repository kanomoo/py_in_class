def e1():
    num = input(">> Program Palindrome Number <<\nEnter integer number : ")
    for i in range(len(num)):
        if num[i] == num[i][::-1]:
            print(f"Diigit {num[i]} equal to Digit {num[i]}")
            result = f"Your enter number : {num} is Palindrome Number."
        else: 
            print(f"Diigit {num[i]} not equal to Digit {num[i]}")
            result = f"Your enter number : {num} is  Not Palindrome Number."
    print(result,"\nExit Program")

def e2():
    num = input(">> Program Change Number to Text <<\nEnter integer number : ")
    t_n = {0:" Zero", 1:" One", 2:" Two", 3:" Three", 4:" Four", 5:" Five", 6:" Six", 7:" Seven", 8:" Eight", 9:" Nine"}
    result = "Text :"
    for i in num:
        if int(i) in t_n: result += t_n[int(i)]
    print(f"Number : {num}\n{result}\nExit Program")

def e3():
    tex = {1_000_000:10, 800_000:7.5, 500_000:5.5, 300_000:4, 150_000:2.5, -1:0,}
    while True:
        num = int(input("Enter your income ( -1 to exit) : "))
        if num == -1: print("Exit Program...");break
        for i in tex:
            if num > i:
                a_tex = num * (tex[i]/100)
                break
        print(f"Net Income : {num:,.2f}\nTax Rate(%) {a_tex:,.2f}\n")

def e4():
    head = "::    Main Menu    ::"
    line = "=" * len(head)
    while True:
        choice = input(f"{line}\n{head}\n{line}\n A. Get Integer Number\n B. Summation of Digit\n C. Count Digit\n D. Exit\nEnter Choice : ").lower()
        print()
        match choice:
            case "a": num = input("Enter long number : ")
            case "b": 
                Max =  sum([int(i) for i in num])
                odd, even = 0, 0
                for i in num:
                    if int(i) % 2 == 0: even += int(i)
                    else: odd += int(i)
                print(f"Your enter number : {num}\nSummation of digit : {Max}\nSummation odd of digit : {odd}\nSummation even of digit : {even}")
            case "c":
                print(f"Your enter number : {num}\nThis number has {len(num)} digits.")
            case "d":
                print("Exit Program...")
                break
        print()

if __name__ == "__main__": 
    e4()