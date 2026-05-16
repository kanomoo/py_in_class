# find non-multiples of three, four, and five
# def find_non_multiples(start: int, end: int) -> list:
#     data = []
#     for i in range(start,end+1):
#         if i % 3 != 0 and i % 4 != 0 and i % 5 != 0:
#             data.append(i)
#     return data

# print(find_non_multiples(10,25))

# output ไม่ตรงตามโจทย์งง

def find_non_multiples(start: int, end: int) -> list:
    num_list = []
    if start >= 1 and end <= 1000 and start < end:
        for i in range(start, end):
            if i % 3 != 0 and i % 4 != 0 and i % 5 != 0: num_list.append(i)
    return num_list

if __name__ == "__main__":
    print(find_non_multiples(10, 25))