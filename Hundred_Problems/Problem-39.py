#remove a word from a sentence

# def remove_word(sentence: str, word_to_remove: str) -> str:
#     return sentence.replace(word_to_remove,"")

def remove_word(sentence: str, word_to_remove: str) -> str:
    sentence = sentence.split()
    result = []
    for i in sentence:
        if i != word_to_remove:
            result.append(i)
    return " ".join(result)

sentence = "Python is a popular programming language."
word_to_remove = "popular"
print(remove_word(sentence, word_to_remove))