# store student scores in a course

def store_student_scores(student_data: list[tuple[str, str, float]]) -> dict[str, dict[str, float]]:
    report = {}
    for num,name,score in student_data:
        re = {"name":name,"score":score}
        report[num] = re
    return report

student_data = [("123456","Alice",85.5),("654321","Bob",92.0),("112233","Charlie",78.0)]
print(store_student_scores(student_data))