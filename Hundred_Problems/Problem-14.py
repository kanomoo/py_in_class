# unique word collector

def collect_unique_words() -> list[str]:
    words = []
    while len(words) < 5:
        word = input("Enter word : ")
        if word.isalpha():
            if word not in words:
                words.append(word)
            else: print("Please input word unique")
        else: print("Please input word")
    return words

print(collect_unique_words())