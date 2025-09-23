#Find Multiples of Three

# def find_multiples_of_three(start: int, end: int) -> list: #-> list หมายถึงฟังก์ชันนี้จะ คืนค่า (return) เป็นชนิด list (ลิสต์)
#     if start > end: return []
#     first = start if start % 3 == 0 else start + (3 - start % 3)
#     return list(range(first, end + 1, 3))
#
# print(find_multiples_of_three(10,25))

# def find_multiples_of_three(start: int, end: int) -> list: #-> list หมายถึงฟังก์ชันนี้จะ คืนค่า (return) เป็นชนิด list (ลิสต์)
#     if start > end: return []
#     if start % 3 == 0:
#         first = start
#     else:
#         first = start + (3 - start % 3)
#     return list(range(first, end + 1, 3))

def find_multiples_of_three(start: int, end: int ) -> list:
    data = []
    for i in range(start,end+1):
        if i % 3 == 0: data.append(i)
    return data

print(find_multiples_of_three(10,25))