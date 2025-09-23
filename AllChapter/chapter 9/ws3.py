from random import randint

fout = open("AllChapter\chapter 9\mydata.txt", "w")
print("Open file myscore.txt")
scores = []
for n in range(10):
    scores.append(str(randint(1,100))+"\n")
print("Now, write score to file.")
scoresStr = []
fout.writelines(scores)
fout.close()
print("Now closed file.")