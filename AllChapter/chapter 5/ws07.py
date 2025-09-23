# total = 0.0
# Max = int(input("Enter number of score : "))
# for n in range(1, Max+1):
#     score = float(input("Enter Score #" + str(n) + " :"))
#     total = total + score
# print()
# print("Total score value : ", total)
# print("Average score : ", total/Max)

total = 0.0
Max = int(input("Enter number of score : "))
message = "Data Input:\n"
for n in range(1, Max+1):
    score = float(input("Enter Score #" + str(n) + " :"))
    total = total + score
    message += "Score #"+ str(n) + " : " + str(score) + "\n"
print(message)
print("Total score value : ", total)
print("Average score : ", total/Max)