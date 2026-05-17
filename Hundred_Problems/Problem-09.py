#average length of strings

# def average_length_of_strings(strings: list[str]) -> float:
#     data = []
#     for i in strings:
#         data.append(len(i))
#     average = sum(data) / 5
#     return average

# def average_length_of_strings(strings: list[str]) -> float:
#     total_length = sum(len(s) for s in strings)
#     return total_length / 5

# print(average_length_of_strings(["apple","Banana","cherry","date","elderberry"]))

def average_length_of_strings(strings: list[str]) -> float:
    length_list = []
    for i in strings:
        if len(i) >= 1 and len(i) <= 100: length_list.append(len(i))
        else: return
    return sum(length_list) / len(strings)

if __name__ == "__main__":
    first_list = ["Apple", "banana", "cherry", "date", "elderberry"]
    print(average_length_of_strings(first_list))