#นายปภาวิน ธิติชุณหกุล 6806021612037
def input_num():
    num = int(input("Enter number : "))
    return num

def find_max_number(num: int) -> str:
    return max(str(num))

def check_palindrome(num: int) -> str:
    return "Palindrome" if str(num)[::-1] == str(num) else "Not Palindrome"

def number_to_text(num: int) -> str:
    text, text_num = "", {0: " Zero", 1: " One", 2: " Two", 3: " Three", 4: " Four", 5: " Five", 6: " Six", 7: " Seven",8: " Eight", 9: " Nine"}
    for i in str(num):
        if int(i) in text_num: text += text_num[int(i)]
    return text

def decimal_to_binary(num: int) -> str:
    binary = ""
    while num != 0:
        binary += str(num % 2)
        num = num // 2
    return binary[::-1]

def report():
    while True:  
        choice = input(f"Program Test Call Module\nMain Menu\n1. Find Max Number\n2. Check Palindrome\n3. Number to Text\n4. Decimal to Binary\n5. Exit\nEnter choice : ")
        match choice:
            case "1":
                num = input_num()
                print(f"Maximum digit {find_max_number(num)} of number {num}.")
            case "2":
                num = input_num()
                print(f"Number {num} is {check_palindrome(num)}.")
            case "3":
                num = input_num()
                print(f"Number : {num}\nText :{number_to_text(num)}")
            case "4":
                num = input_num()
                print(f"Decimal number : {num}\nBinary number : {decimal_to_binary(num)}")
            case "5":
                print(f"Exit Program.")
                break
        print()

