# find multiples of both three and four
# def find_multiples_of_three_and_four(start: int, end: int ) -> list:
#     data = []
#     for i in range(start,end+1):
#         if i % 3 == 0 and i % 4 == 0: data.append(i)
#     return data

# print(find_multiples_of_three_and_four(10,50))

def find_multiples_of_three_and_four(start: int, end: int) -> list:
    num_list = []
    if start >= 1 and end <= 1000 and start < end:
        for i in range(start, end):
            if i % 3 == 0 and i % 4 == 0 and i: num_list.append(i)
    return num_list

if __name__ == "__main__":
    print(find_multiples_of_three_and_four(10, 50))