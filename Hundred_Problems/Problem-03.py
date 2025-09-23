# find non-multiples of three, four, and five
def find_non_multiples(start: int, end: int) -> list:
    data = []
    for i in range(start,end+1):
        if i % 3 != 0 and i % 4 != 0 and i % 5 != 0:
            data.append(i)
    return data

print(find_non_multiples(10,25))

# output ไม่ตรงตามโจทย์งง