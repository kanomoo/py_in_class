# def check_palindrome(num):
#     result = ""
#     for i in range(len(str(num))):
#         if str(num)[i] == str(num)[len(str(num)) - (i+1)]: result = True
#         else: result = False
#     return result
#
# print(check_palindrome(12344321))

def check_palindrome(num):
    result, num = "", str(num)
    for i in range(len(num)):
        if num[i] == num[len(num) - (i+1)]: result = True
        else: result = False
    return result

print(check_palindrome(12344321))


# def check_palindrome(num):
#     if str(num) == str(num)[::-1]: return True
#     else: return False
#
# print(check_palindrome(12344321))