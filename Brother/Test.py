num = int(input())
for i in range(1,num+1):
    print(" " * (num - int(i)), "*" * i, "*" * (int(i) - 1),sep="")
for i in range(num-1,0,-1):
    print(" " * (num - int(i)),"*" * i,"*" * (int(i)-1),sep="")