# count word occurrences

# def count_word_occurrences(words: list[str]) -> dict[str, int]:
#     output = {}
#     for i in words:
#         output[i] = words.count(i)
#     return output

def count_word_occurrences(words: list[str]) -> dict[str, int]:
    output = {}
    for i in words:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
    return output

print(count_word_occurrences(["apple","banana","apple","orange","banana","apple"]))