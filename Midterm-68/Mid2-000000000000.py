# ชือ (งานนี้ 8 คะแนน)
print(">> Program Calculator <<\n")
total = 0
for i in range(5):
    num = int(input(f"Enter number #{i+1} : "))
    total += num
print(f"\nTotal number : {total}\nAverage number : {total / 5:.2f}")