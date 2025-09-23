# from random import randint

# def randomScores(scores):
#     for n in range(1,11):
#         scores[n] = randint(30,100)
    
# def checkGrade(scores,grades):
#     GRADES = {80:"A",70:"B",60:"C",50:"D",0:"F"}
#     for n, score in scores.items():
#         for key, value in GRADES.items():
#             if (score >= key):
#                 grades[n] = value
#                 break

# def reportGrade(scores, grades):
#     print("=" * 23)
#     print("| No. | Score | Grade |")
#     print("=" * 23)
#     for n in scores:
#         print(f"| %3d |  %3d  |  %s  |"%(n, scores[n],grades[n]))
#     print("=" * 23)

# scores = {}
# grades = {}
# randomScores(scores)
# print(scores)
# checkGrade(scores,grades)
# print(grades)
# reportGrade(scores,grades)


# =======================================
from random import randint

def scores():
    score, grades = {}, {}
    GRADES = {80:"A",70:"B",60:"C",50:"D",0:"F"}
    for i in range(10):
        rd = randint(0,100)
        score[i+1] = rd
        for grade in GRADES:
            if score[i+1] >= grade: 
                grades[i+1] = GRADES[grade]
                break
    return score, grades

def report(score,grades):
    result = ""
    head = "| No. | Score | Grade |"
    line = "=" * len(head)
    result += f"{line}\n{head}\n{line}\n" 
    for i in range(len(score)):
        result += f"|  {i+1:2} |  {score[i+1]:3}  |   {grades[i+1]}   |\n"
    print(result+line)

def main():
    score, grades = scores()
    report(score,grades)

if __name__ == "__main__":
    main()