# sum of corresponding elements in two matrices

# def remove_word_from_list(words: list[str], word: str) -> list[str]:
#     if word in words:
#         words.remove(word)
#     return words

# words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
# "honeydew", "kiwi", "lemon"]
# word = "cherry"
# print(remove_word_from_list(words, word))


def remove_word_from_list(words: list[str], word:str) -> list[str]:
    if len(words) != 10: return "word out of range"
    if word in words:
        words.remove(word.strip())
        return words
    else: return "unchanged"

if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    print(remove_word_from_list(word_list, "cherry"))