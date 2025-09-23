# name = input()
# for i in name:
#     if i.isdigit(): continue
#     print(i)

# name,n,a,b,c,mess = "A111B222C333",0,0,0,0,""
# for i in name:
#     if i == "A":
#         a += 1
#         mess += i
#     elif i == "B":
#         b += 1
#         mess += i
#     elif i == "C":
#         c += 1
#         mess += i
#     if i in ["A","B","C"]: n += 1
# print(a,b,c,n,mess)

# n = 0
# for i in range(1,11):
#     if i % 2 == 0 :
#         n += 1
#         print(i)
# print(n)
#

# months = int(input())
# m = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# print(m[months]) if months in m.keys()else print("ไม่มีเดือน")





# p = 123521
# for i in range(len(str(p))//2):
#


#p = 123521
#n1 = p // 10000
#r1 = p % 10
#n2 = p % 10000 // 1000
#r2 = p % 100 // 10
#n3 = p % 1000 // 100
#r3 = p % 1000 // 100
#if n1 == r1 and r2 == r2: print("Palindrome")
# else: print("Not Palindrome")

# n = 0
# for i in range(1,101):
#     if i % 7 == 0 :
#         n += 1
#         print(i)
#     if n == 5: break

# n,total = 0,0
# while True:
#     n += 1
#     num = int(input(f"Day {n}: "))
#     total += num
#     if total >= 1000 :
#         print(f"ครบ 1000 บาท ใน {n} วัน")
#         break

# n,total = 0,0
# while True:
#     n += 1
#     num = int(input(f"Day {n}: "))
#     total += num
#     if total >= 1000 :
#         print(f"ครบ 1000 บาท ใน {n} วัน")
#         break

head = f"|{"No":^20}|{"Name":^20}|{"Age":^20}|{"Birthday":^20}|"
line = "=" * len(head)
print(line,head,line,sep="\n")
for i in range(1,9):
    print(f"|{i:<20}|{"Hello Python":^20}|{"45":^20}|{"01 Feb 1980":>20}|" )
print(line)

# total = [i for i in range(1,101)]
# print(sum(total))




