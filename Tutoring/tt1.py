from TT1.CarModule import *
def tt1():
    def main():
        while True:
            choice = input(f"{"=" * 32}\n|{"Menu Installment":^30}|\n{"-" * 32}\n|{" 1. Add installment":30}|\n|{" 2. Edit installment":30}|\n|{" 3. Delete installment":30}|\n|{" 4. Report installment":30}|\n|{" 5. Exit":30}|\n{"=" * 32}\nEnter choice : ")
            match choice:
                case "1":
                    add_and_save(r"Tutoring/TT1/CarInstallment.txt")
                case "2":
                    edit_installment(r"Tutoring/TT1/CarInstallment.txt")
                case "3":
                    del_installment(r"Tutoring/TT1/CarInstallment.txt")
                case "4":
                    report_installment(r"Tutoring/TT1/CarInstallment.txt")
                case "5":
                    print("\nEixt Program...")
                    exit()
            print()

    if __name__ == "__main__":
        main()


if __name__ == "__main__":
    tt1()