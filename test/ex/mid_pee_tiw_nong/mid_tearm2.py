name = "Nahee"

# for n in range(len(name)): # 0 1 2 3 4 5 6
#
#     for i in range(len(name) -n -1,-1,-1):  #    3 2 1 0
#         print(name[i],end="")
#
#     for i in range(len(name)):
#         print(" " * (n*2),end="")
#         break
#
#     for i in range(n,len(name)):
#         print(name[i],end="")
#
#     print()

nane = "Kanokphon" #6
for i in range(len(name)): # 0 1 2 3 4 5
    print(name[::-1][:len(name)-i]," " * i, " " * i ,name[i:],sep="")