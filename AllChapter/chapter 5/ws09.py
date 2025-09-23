Total = 0.0
Score = ""
Count = 0
while Score != "-1":
    Score = input("Enter score value #"+str(Count+1)+ " : ")
    if Score != "-1":
        Count += 1
        Total += float(Score)

print()
print("Number of Score : ", Count)
print("Total Score value : ", Total)
print("Average Score : ", Total/Count)