#prime number checker
# def check_prime(n: int) -> str:
#     data = []
#     if n <= 1: return "is not prime"
#     for i in range(1,n+1):
#         if n % i == 0:
#             data.append(i)
#     if len(data) <= 2: return "is prime"
#     else: return "is not prime"


def check_prime(n: int) -> str:
    if n <= 1: return "is not prime"
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2: return "is prime"
    else: return "is not prime"


# def check_prime(n: int) -> str:
#     if n <= 1:
#         return "is not prime"
#
#     for i in range(2, int(n ** 0.5) + 1):  # ใช้ square root เพื่อลดจำนวนรอบ
#         if n % i == 0:
#             return "is not prime"
#
#     return "is prime"


print(check_prime(17))