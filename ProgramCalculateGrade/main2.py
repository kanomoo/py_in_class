def calculate_grade(score):
    if score >= 80:
        return 'A', 4.0
    elif score >= 70:
        return 'B', 3.0
    elif score >= 60:
        return 'C', 2.0
    elif score >= 50:
        return 'D', 1.0
    else:
        return 'F', 0.0

def main():
    subjects = []
    total_credits = 0
    total_points = 0

    for i in range(1, 7):
        score = float(input(f"Enter score of subject #{i}: "))
        credit = int(input(f"Enter credit of subject #{i}: "))
        grade, point = calculate_grade(score)
        subjects.append((i, score, grade, credit, point * credit))
        total_credits += credit
        total_points += point * credit

    print("\n           Report Grade")
    print("===================================")
    print("|No.|  Mark  |Grade|Credit| Points|")
    print("===================================")
    for sub in subjects:
        print(f"| {sub[0]} | {sub[1]:6.1f} |  {sub[2]}  |   {sub[3]}  | {sub[4]:6.1f} |")
    print("===================================")
    print(f"|        Total     | {total_credits:3}  | {total_points:6.1f} |")
    print("===================================")
    print(f"Grade Point Average(GPA) : {total_points / total_credits:.2f}")

if __name__ == "__main__":
    main()