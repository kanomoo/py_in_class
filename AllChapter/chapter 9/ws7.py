def read_data():
    with open("AllChapter\chapter 9\mydata.txt", encoding="utf-8") as fin:
        data = fin.readline()
        while (data != ""):
            print(data)
            data = fin.readline()
    print("finish read.\n")

def read_and_write():
    with open("AllChapter\chapter 9\mydata.txt", encoding="utf-8") as fin, \
        open("AllChapter\chapter 9\myoutput.txt","w", encoding="utf-8") as fout:
        for line in fin:
            print(line)
            fout.writelines(line)
    print("finish read and write file.\n")

def main():
    menu = "Main menu\n===========\n1. Read Data\n2. Read and write\n"
    menu += "3.Exit\nEnter Choice : "
    while True:
        choice = input(menu)
        if choice == "1":
            read_data()
        elif choice == "2":
            read_and_write()
        elif choice == "3":
            print("Exit program")
            break

if __name__ == "__main__":
    main()