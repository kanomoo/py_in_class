#
# print("Input Data:")
# datas = []
# total_p = 0
# total_c = 0
# for i in range(1,6):
#     data = []
#     name = input(f"Enter subject name({i}) : ")
#     score = int(input(f"Enter subject score({i}) : "))
#     print()
#     data.append(i)
#     data.append(name)
#     data.append(score)
#     g = {80:"A",70:"B",60:"C",50:"D",0:"F"}
#     for i in g:
#         if score >= i:
#             grade = g[i]
#             data.append(grade)
#             break
#     p = {"A":4,"B":3,"C":2,"D":1,"F":0}
#     for i in p:
#         if grade == i:
#             point = p[i] * 3
#             data.append(format(point,".2f"))
#             break
#     total_p += point
#     total_c += 3
#     datas.append(data)
# head = "No. Subject Name        Mark  Grade    Points   "
# line = "=" * len(head)
# print(format("Grade Point Average(GPA) Report","^48"))
# print(line,head,line,sep="\n")
# for i in datas:
#     print(f"{i[0]}   {i[1]:<21}{i[2]}      {i[3]}      {i[4]}")
# print(line)
# print(f"Total Points :{total_p:.1f}")
# print(f"Total Credit :{total_c:.1f}")
# print(f"Grade Point Average(GPA) :{total_p / total_c:.2f}")


# #ทำไว้ show ใน terminal
# print("Input Data:")
# datas = []
# total_p = 0
# total_c = 0
# for i in range(1,6):
#     data = []
#     name = ["English","Compro","Fun IT","General math","Problem Solving"]
#     score = [80,80,80,65,60]
#     name = name[i-1]
#     score = score[i-1]
#     print(f"Enter subject name({i}) : {name}")
#     print(f"Enter subject score({i}) : {score}")
#     print()
#     data.append(i)
#     data.append(name)
#     data.append(score)
#     g = {80:"A",70:"B",60:"C",50:"D",0:"F"}
#     for i in g:
#         if score >= i:
#             grade = g[i]
#             data.append(grade)
#             break
#     p = {"A":4,"B":3,"C":2,"D":1,"F":0}
#     for i in p:
#         if grade == i:
#             point = p[i] * 3
#             data.append(format(point,".2f"))
#             break
#     total_p += point
#     total_c += 3
#     datas.append(data)
# head = "No. Subject Name        Mark  Grade    Points   "
# line = "=" * len(head)
# print(format("Grade Point Average(GPA) Report","^48"))
# print(line,head,line,sep="\n")
# for i in datas:
#     print(f"{i[0]}   {i[1]:<21}{i[2]}      {i[3]}      {i[4]}")
# print(line)
# print(f"Total Points :{total_p:.1f}")
# print(f"Total Credit :{total_c:.1f}")
# print(f"Grade Point Average(GPA) :{total_p / total_c:.2f}")

print("Input Data:")
result,t_p,t_c = "",0,0
for i in range(1,6):
    name = input(f"Enter subject name({i}) : ")
    score = int(input(f"Enter subject score({i}) : "))
    if 80 <= score <= 100: grade,point = "A",4.0 * 3.0
    elif score >= 70: grade,point = "B",3.0 * 3.0
    elif score >= 60: grade,point = "C",2.0 * 3.0
    elif score >= 50: grade,point = "D",1.0 * 3.0
    else: grade,point = "F",0.0 * 3.0
    t_p += point
    t_c += 3.0
    result += f"{i}    {name:23}{score}     {grade}      {point}\n"
    print()
head = f"No. Subject Name          Mark  Grade    Points   "
line = "=" * len(head)
result += line
print(f"{"Grade Point Average(GPA) Report)":^{len(head)}}")
print(line,head,line,result,f"Total Points :{t_p}",f"Total Credit :{t_c}",f"Grade Point Average(GPA) :{t_p / t_c:.2f}",sep="\n")

