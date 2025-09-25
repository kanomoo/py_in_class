def Max():
    num = input("Enter number : ")
    print(f"Maximum digit {max(str(num))} of number {num}\n")

def palindrome():
    p = ""
    count = [0,-1]
    num = input("Enter number : ")
    for i in num:
        if num[count[0]] == num[count[1]]:
            p = f"Number {num} is Palindrome.\n"
        elif num[count[0]] != num[count[1]]:
            p = f"Number {num} not Palindrome.\n"
        count[0] += 1
        count[1] -= 1
    print(p)

def num_text():
    text = ""
    num = input("Enter number : ")
    for i in num:
        if i == "9": text += "Nine "
        elif i == "8": text += "Eight "
        elif i == "7": text += "Seven "
        elif i == "6": text += "Sic "
        elif i == "5": text += "Five "
        elif i == "4": text += "Four "
        elif i == "3": text += "Three "
        elif i == "2": text += "Two "
        elif i == "1": text += "Onw "
        elif i == "0": text += "Zero "
        else: pass
    print(f"Number : {num}\nText : {text}\n")

def binary():
    num = int(input("Enter decimal number : "))
    print(f"Decimal number : {num}\nBinary number : {bin(num)[2:]}\n")
