#check for vowel presence in a string

def contains_vowel(s: str) -> bool:
    vowel = ["a","e","i","o","u"]
    for i in s:
        i = i.lower()
        if i in vowel:
            return True
    return False

print(contains_vowel("HELLO WORLD"))