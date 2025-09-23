# set operations

# def set_operations(set1: set, set2: set) -> tuple[set, set]:
#     union = set1.union(set2)
#     intersection = set1.intersection(set2)
#     return  union,intersection

def set_operations(set1: set, set2: set) -> tuple[set, set]:
    union = set1 | set2 # or
    intersection = set1 & set2 # and
    return  union,intersection

set1 = {'a', 'e', 'i', 'o', 'u'}
set2 = {'h', 'e', 'l', 'l', 'o'}
print(set_operations(set1, set2))