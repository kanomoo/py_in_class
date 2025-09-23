#insert new words at the front of a list

def insert_at_front(words: list[str]) -> list[str]:
    re = []
    for i in words:
        re.insert(0,i) # .insert(index, item)
    return re
print(insert_at_front(["apple", "banana", "cherry"]))