#prime number in a range

# def prime_numbers_in_range(start: int, end:int) -> tuple:
#     data = []
#     for i in range(start,end+1):
#         count = 0
#         for n in range(2,i):
#             if i % n == 0:
#                 break
#             else:
#                 data.append(i)
#         if count == 1:
#             data.append(i)
#     return (data,sum(data)) # การเขียนค่าหลายๆ ค่าในวงเล็บ ( , ) จะกลายเป็น tuple โดยอัตโนมัติ
#
# print(prime_numbers_in_range(10,20))


# def prime_numbers_in_range(start: int, end:int) -> tuple:
#     data = []
#     for i in range(start,end+1):
#         for n in range(2,i):
#             if i % n == 0:
#                 break
#         else:
#             data.append(i)
#     return data,sum(data)

# print(prime_numbers_in_range(10,20))
import math

def prime_numbers_in_range(start: int, end: int) -> tuple:
    prime_list = []
    if start >= 1 and start <= 1000 and end >= 1 and end <= 1000:
        for i in range(start, end + 1):
            for n in range(2, round(math.sqrt(i)) + 1):
                if i % n == 0: break
            else: prime_list.append(i)
        return prime_list, sum(prime_list)

if __name__ == "__main__":
    print(prime_numbers_in_range(10, 20))