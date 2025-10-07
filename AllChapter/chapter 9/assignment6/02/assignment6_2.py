#นายปภาวิน ธิติชุณหกุล 6806021612037
from ScoreModule import *

def main():
    while True:
        choice = input("Main Menu\n---------------\n 1. Add score student\n 2. Report Grade of Student\n 3. Exit\nEnter Choicce : ")
        match choice:
            case "1": add_sccore()
            case "2": report_score()
            case "3": 
                print("Exit Program.")
                exit()
        print("")

if __name__ == "__main__":
    main()