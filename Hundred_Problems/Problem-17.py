# word search in list

# def is_word_in_list(word_list: list[str], search_term: str) -> bool:
#     if search_term in word_list:
#         return True
#     else: return False

# def is_word_in_list(word_list: list[str], search_term: str) -> bool:
#     return search_term.lower() in word_list

# word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
# "kiwi", "lemon"]
# search_term = "cherry"
# print(is_word_in_list(word_list, search_term))

def is_word_in_list(word_list: list[str], search_term: str) -> bool:
    if len(word_list) != 10: return "word list out of range"
    for i in word_list:
        if (len(i) >= 1 and len(i) <= 100) and (len(search_term) >= 1 and len(search_term) <= 100):
            if i == search_term: return True
        else: return "each word and search_term out of range"
    else: return False

if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    print(is_word_in_list(word_list, "lemon"))