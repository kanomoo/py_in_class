# find all divisors of a given number

# def find_divisors(num: int) -> list:
#     result = []
#     for i in range(1,num+1):
#         if num % i == 0:
#             result.append(i)
#     return result

# print(find_divisors(12))


def find_divisors(num: int) -> list:
    return [n for n in range(1, num + 1) if num % n == 0]

if __name__ == "__main__":
    print(find_divisors(12))