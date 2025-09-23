print("Program Calculate Grade\n")
print("Input Data:")
scores = ()
grades = ()
credits = ()
points = ()
total_credit = 0
total_point = 0
for i in range(1,7):
    score = int(input(f"Enter score of subject  #{i} : "))
    credit = int(input(f"Enter credit of subject #{i} : "))
    scores += (score,)
    credits += (credit,)
    if score >= 80: t = "A", 4
    elif score >= 70: t = "B",3
    elif score >= 60: t = "C", 2
    elif score >= 50: t = "D", 1
    else:t = "F", 0
    grade, point = t
    grades += (grade,)
    points += (point,)
    total_credit += credit
    total_point += point * credit
print("\n         Report Grade")
l = ("|No.|  Mark  |Grade|Credit| Points|")
print("=" * len(l))
print(l)
print("=" * len(l))
for i in range(len(scores)):
    print(f"| {i+1} |  {scores[i]:.1f}  |  {grades[i]}  |   {credits[i]}  | {(credits[i] * points[i]):5.1f} |")
print("=" * len(l))
print(f"|       Total      | {total_credit:.1f} |  {total_point:.1f} |")
print("=" * len(l))
print(f"Grade Point Average(GPA) : {total_point / total_credit:.2f}")
