# find words of specified length

def find_words_of_length(words: list[str], length: int) -> list[str]:
    result = []
    for i in words:
        if len(i) == length:
            result.append(i)
    return result

words = ["apple", "banana", "cherry", "date", "fig", "grape"]
length = 5
print(find_words_of_length(words, length))