# from random import randint

# fout = open("AllChapter\chapter 9\mydata.txt", "w")
# print("Open file myscore.txt")
# scores = []
# for n in range(10):
#     scores.append(str(randint(1,100))+"\n")
# print("Now, write score to file.")
# scoresStr = []
# fout.writelines(scores)
# fout.close()
# print("Now closed file.")

from random import randint

with open("AllChapter\chapter 9\mydata.txt", "w", encoding="utf-8") as fout:
    for i in range(10): fout.write(str(randint(0,100))+"\n")
