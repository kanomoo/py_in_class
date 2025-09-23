#average length of strings

# def average_length_of_strings(strings: list[str]) -> float:
#     data = []
#     for i in strings:
#         data.append(len(i))
#     average = sum(data) / 5
#     return average

def average_length_of_strings(strings: list[str]) -> float:
    total_length = sum(len(s) for s in strings)
    return total_length / 5

print(average_length_of_strings(["apple","Banana","cherry","date","elderberry"]))