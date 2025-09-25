import random

def input_scores():
    scores = {}
    total = 0
    while True:
        score = int(input("Enter number of score (enter -1 to finish): "))
        if score == -1:
            break
        grade = input("Enter grade (A, B, C, D, F): ").upper()
        if grade in scores:
            scores[grade] += score
        else:
            scores[grade] = score
        total += score
    return scores, total


def random_scores():
    scores = {'A': random.randint(0, 30), 'B': random.randint(0, 30),
              'C': random.randint(0, 30), 'D': random.randint(0, 30),
              'F': random.randint(0, 30)}
    total = sum(scores.values())
    return scores, total


def check_grades():
    print("-----------------")
    print("| Grade | Total |")
    print("-----------------")
    for grade, total in scores.items():
        print(f"|   {grade}   |  {total}  |")
    print("-----------------")
    print(f"| Total | {total} |")
    print("-----------------")


# Main program
while True:
    print("Main Menu")
    print("==========")
    print("1. Input Number of Score")
    print("2. Random Score and Check Grade")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        scores, total = input_scores()
    elif choice == 2:
        scores, total = random_scores()
        check_grades()
    elif choice == 3:
        print("Exit Program")
        break
    else:
        print("Choice not correct.")
