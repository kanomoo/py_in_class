from module.SaleModule import *
from module.ScoreModule import *

def t1():
    def main():
        print('\nRandom sale and save to file "sale.txt".\n')
        random_and_save_sale("Tutoring\module\sale.txt",15,7)
        report("Tutoring\module\sale.txt")

    if __name__ == "__main__":
        main()

def t2():
    def main():
        while True:
            choice = input(f"Main Menu\n------------\n 1. Add score student\n 2. Report Grade of Student\n 3. Exit\nEnter Choice : ")
            match choice:
                case "1":
                    add_score("Tutoring\module\sale2.txt")
                case "2":
                    report_score("Tutoring\module\sale2.txt")
                case "3":
                    exit()
            print()

    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    t2()