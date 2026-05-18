#insert new words at the front of a list

# def insert_at_front(words: list[str]) -> list[str]:
#     re = []
#     for i in words:
#         re.insert(0,i) # .insert(index, item)
#     return re
# print(insert_at_front(["apple", "banana", "cherry"]))


def insert_at_front(words: list[str]) -> list[str]:
    words_list = []
    for i in words: words_list.insert(0, i)
    return words_list

if __name__ == "__main__":
    print(insert_at_front(["apple", "banana", "cherry"]))