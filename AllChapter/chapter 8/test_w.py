# 8_1
# def input_sale():
#     sales = ()
#     for i in range(7):
#         sale = int(input(f"Enter sale day {i+1} : "))
#         sales += (sale,)
#     return sales

# def total_sale(sales : tuple):
#     return sum(sales)

# def com(total):
#     # rate = {20000:10,10000:7.5,5000:5,1000:2.5,1:0}
#     r_com = (20000,10000,5000,1000,1)
#     rate = (10,7.5,5,2.5,1)
#     for i in range(len(rate)):
#         if total > r_com[i]: return rate[i]
#     return None


# def report():
#     result = ""
#     total = total_sale(input_sale())
#     rate = com(total)
#     result += f"\nTotal sale : {total:.2f}\nCommission rate : {rate:.2f}%\nTotal commission : {total * rate / 100:.2f}"
#     print(result)

# report()

# ==============================


def input_score():
    # scores, score, i = [], None, 0
    scores, score, i = (), None, 0

    while True:
        i += 1
        if score != -1:
            score = int(input(f"Enter score {i} ( -1 to exit): "))
            scores += (score,)
        else: return scores

def s_grade(scores):
    grades = ()
    score = (80, 70, 60, 50, 0)
    grade = ("A", "B", "C", "D", "F")
    for i in scores:
        for n in range(len(score)):
            if i > score[n]:
                grades += (grade[n],)
                break
    return grades

def report(scores,grades):
    print(scores)
    print(grades)
    result = ""
    head = "| No. | Scores | Grade |"
    line = "=" * len(head)
    result += f"{line}\n{head}\n{line}"
    for i in range(len(scores)):
        result += f"|  {i}  |   {scores[i]:3}  |   {grades[i]}   |"
    result += f"{line}\nEnd Program."
    return result


scores = input_score()
grades = s_grade(scores)
print(report(scores,grades))
