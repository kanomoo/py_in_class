# s = input("Enter string : ")
# s_len = len(s)

# if s_len > 10:
#     print("Your string length :", s_len)
# print("Your string enter is", s)

s = input("Enter string : ")
print(f"Your string length : {len(s)}") if len(s) > 10 else print(f"Your string enter is {s}")  