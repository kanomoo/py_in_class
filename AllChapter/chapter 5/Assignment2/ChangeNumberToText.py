#นายปภาวิน ธิติชุณหกุล 6806021612037
print(">> Program Change Number To Text")
num,result = input("Enter integer number : "),"Text : "
print(f"Number : {num}")
for i in num: #แสดงchar ใน num ทีละตัว
    if i == "0": result += "Zero "
    elif i == "1": result += "One "
    elif i == "2": result += "Two "
    elif i == "3": result += "Three "
    elif i == "4": result += "Four "
    elif i == "5": result += "Five "
    elif i == "6": result += "Six "
    elif i == "7": result += "Seven "
    elif i == "8": result += "Eight "
    elif i == "9": result += "Nine "
print(result,"Exit Program",sep="\n")

