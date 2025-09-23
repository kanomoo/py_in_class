Done = True
Count = 0
while Done:
    Score = input("Enter score value #"+str(Count+1)+" : ")
    if Score != "-1":
        Mark = float(Score)
        if Mark >= 0 and Mark <= 100:
            Grade = ""
            if Mark >= 80:
                Grade = "A"
            elif Mark >= 70:
                Grade = "B"
            elif Mark >= 60:
                Grade = "C"
            elif Mark >= 50:
                Grade = "D"
            else: 
                Grade = "F"
            print("Score is "+str(Mark)+", get " +Grade)
            Count += 1
        else:
            print("Score out of range, input again.")
    elif Score == "-1":
        Done = False
        
print("Exit Program")