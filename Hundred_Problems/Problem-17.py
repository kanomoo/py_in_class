# word search in list

# def is_word_in_list(word_list: list[str], search_term: str) -> bool:
#     if search_term in word_list:
#         return True
#     else: return False

def is_word_in_list(word_list: list[str], search_term: str) -> bool:
    return search_term.lower() in word_list

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
"kiwi", "lemon"]
search_term = "cherry"
print(is_word_in_list(word_list, search_term))