from TT3.ScoreModule import *

def main():
    while True:
        choice = input(" Main Menu\n----------\n 1. Add Score student\n 2. Report Grade of Student\n 3. Edit Score\n 4. Del Score\n 5. Exit\nEnter Choice : ")
        match choice:
            case "1": 
                add_score(r"Tutoring/TT3/score.txt")
            case "2":
                report_score(r"Tutoring/TT3/score.txt")
            case "3":
                edit_score(r"Tutoring/TT3/score.txt")
            case "4":
                del_score(r"Tutoring/TT3/score.txt")
            case "5":
                print("\nExit Program...")
                exit()
        print()

if __name__ == "__main__":
    main()