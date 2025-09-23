# compare the length of two strings

def compare_string_lengths(str1: str, str2: str) -> str:
    if len(str1) > len(str2):
        return f"The first string is longer by {len(str1) - len(str2)} character(s)."
    elif len(str1) < len(str2):
        return f"The second string is loger by {len(str2) - len(str1)} character(s)."
    else:
        return ""
    
str1 = "apple"
str2 = "banana"
print(compare_string_lengths(str1, str2))