# find multiples of both three and four
def find_multiples_of_three_and_four(start: int, end: int ) -> list:
    data = []
    for i in range(start,end+1):
        if i % 3 == 0 and i % 4 == 0: data.append(i)
    return data

print(find_multiples_of_three_and_four(10,50))