score = 0
subject = []
t_c = 0
t_p = 0
print("Program Calculate Grade")
print("\nInput Data:")
for i in range(1,7):
    score = float(input(f"Enter score of subject  #{i} : "))
    if score >= 80:
        t = 'A', 4.00
    elif score >= 70:
        t = 'B', 3.00
    elif score >= 60:
        t = 'C', 2.00
    elif score >= 50:
        t = 'D', 1.00
    else:
        t = 'F', 0.00
    grade, point = t
    credit = int(input(f"Enter credit of subject #{i} : "))
    subject.append((i, score, grade, credit,point * credit))
    t_c += credit
    t_p += point * credit
print("\n           Report Grade")
print("|No.|  Mark |Grade|Credit| Points|")
print("==================================")
for s in subject:
    print(f"| {s[0]} |  {s[1]} |  {s[2]}  |   {s[3]}  |  {s[4]:4.1f} |")
print("==================================")
print(f"|       Total     | {t_c:.1f} |  {t_p:4.1f} |")
print("==================================")
print(f"Grade Point Average(GPA) : {t_p / t_c:.2f}")