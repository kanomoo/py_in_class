#check for vowel presence in a string

# def contains_vowel(s: str) -> bool:
#     vowel = ["a","e","i","o","u"]
#     for i in s:
#         i = i.lower()
#         if i in vowel:
#             return True
#     return False

# print(contains_vowel("HELLO WORLD"))



def contains_vowel(s: str) -> bool:
    if len(s) >= 1 and len(s) <= 100:
        for i in s:
            if i in ["a", "e", "i", "o", "u"]: return True
        return False
    return "string out of length"

if __name__ == "__main__":
    print(contains_vowel("Hello World"))