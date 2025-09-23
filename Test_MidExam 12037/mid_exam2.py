# นายปภาวิน ธิติชุณหกุล 6806021612037 it sec.c
name = input("Inpu Text: ")
for i in range(len(name)):
    print(name[::-1][:len(name)-i]," " * i," " * i,name[i:],sep="")