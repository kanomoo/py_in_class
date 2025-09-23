import math
print()
result = ""
result += ("=" * 40 +"\n")
result += ("|Angle|   Sin    |   Cos    |  Tan     |\n")
result += ("=" * 40 +"\n")
for angle in range(0, 361, 20):
    radian = math.radians(angle)
    result += (f"|%4d |" % angle)
    result += ("%9.5f |" % math.sin(radian))
    result += ("%9.5f |" % math.cos(radian))
    result += ("%9.5f |" % math.tan(radian) + "\n")
result += ("=" * 40)
print(result)

# import math
# head = "|Angle|   Sin    |   Cos    |   Tan    |"
# line = len(head) * "="
# print(line,head,line,sep="\n")
# for i in range(0,361,20):
#     r = math.radians(i)
#     print(f"|{i:4} |{math.sin(r):9.5f} |{math.cos(r):9.5f} |{math.tan(r):9.5f} |")
# print(line)