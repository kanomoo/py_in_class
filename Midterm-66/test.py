names, scores, grades, points, = [],[],[],[]
print("Input Data:")
for i in range(5):
    name = input(f"Enter subject name({i+1}) : ")
    score = int(input(f"Enter subject score({i+1}) : "))
    g = {80:("A",4),70:("B",3),60:"C",50:"D",0:"F"}
    for k,v in g.items():
        if score >= k:
            grade,point = g[k]
            grades.append(grade)
            points.append(point * 3)
            break
    print()
    names.append(name)
    scores.append(score)
print("Grade Point Average(GPA) Report")
head = "No. Subject Name        Mark  Grade    Points"
line = "=" * (len(head) + 3)
print(line,head,line,sep="\n")
for i in range(5):
    print(f"{i} {names[i]} {scores[i]} {grades[i]} {points[i]}")

