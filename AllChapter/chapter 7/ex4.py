# def dec_to_bin(num):
#     result, n = "", 0
#     while num != 0:
#         n += 1
#         result += str(num % 2)
#         num = num // 2
#         if n % 4 == 0: result += " "
#     return result[::-1].strip()
#
# print(dec_to_bin(142))

def dec_to_bin(num):
    result, n  = "", 0
    for i in bin(num)[2:]:
        result += i
        n += 1
        if n % 4 == 0 and n != len(bin(num)[2:]): result += " "
    return result

print(dec_to_bin(142))