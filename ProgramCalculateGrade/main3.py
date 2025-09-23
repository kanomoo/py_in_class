def calculate(score):
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
    subject = []
    total_score = 0
    total_credit = 0
    print("Program Calculate Grade")
    print("\nInputer Data:")
    for i in range(1,7):
        score = float(input(f"Enter score of subject  #{i} : "))
        credit = int(input(f"Enter credit of subject #{i} : "))
        grade, point = calculate(score)
        total_score += point * credit
        total_credit += float(credit)
        subject.append((i, score, grade, credit, credit * point))
    print("\n          Report Grade")
    print("==================================")
    print("|No.|  Mark |Grade|Credit| Points|")
    print("==================================")
    for s in subject:
        print(f"| {s[0]} |  {s[1]} |  {s[2]}  |   {s[3]}  |  {s[4]:4.1f} |")
    print("==================================")
    print(f"|        Total    | {total_credit} |  {total_score:4.1f} |")
    print("==================================")
    print(f"Grade Point Average(GPA) : {total_score / total_credit:.2f}")

if __name__ == "__main__":
    main()