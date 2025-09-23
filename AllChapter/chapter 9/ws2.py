data1 = ["Somchai", "Cheingpongpan", "\n"]
data2 = ("Python", "File", "\n")
data3 = {"name":"Somchai","surname":"Cheingpongpan"}
fout = open("AllChapter\chapter 9\mydata.txt","w")
print(fout.write("Hello, text file\n"))
fout.write("Salary : " + str(1200.5)+"\n")
fout.writelines(data1)
fout.writelines(data2)
fout.writelines(data3)
fout.close