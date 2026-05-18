# count word occurrences

# def count_word_occurrences(words: list[str]) -> dict[str, int]:
#     output = {}
#     for i in words:
#         output[i] = words.count(i)
#     return output

# def count_word_occurrences(words: list[str]) -> dict[str, int]:
#     output = {}
#     for i in words:
#         if i in output:
#             output[i] += 1
#         else:
#             output[i] = 1
#     return output

# print(count_word_occurrences(["apple","banana","apple","orange","banana","apple"]))

def count_word_occurrences(words: list[str]) -> dict[str, int]:
    words_dict = {}
    for i in words:
        if words_dict.get(i, 1) >= 1 and words_dict.get(i, 1) <= 100: words_dict[i] = words_dict.get(i, 0) + 1
        else: return "word out of range number"
    return words_dict

if __name__ == "__main__":
    words_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    print(count_word_occurrences(words_list))