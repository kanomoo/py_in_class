# sum of corresponding elements in two matrices

def remove_word_from_list(words: list[str], word: str) -> list[str]:
    if word in words:
        words.remove(word)
    return words

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
"honeydew", "kiwi", "lemon"]
word = "cherry"
print(remove_word_from_list(words, word))