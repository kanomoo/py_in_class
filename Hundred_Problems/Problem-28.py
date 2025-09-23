# check membership in set

# def check_membership(s: set, value: str) -> bool:
#     return value in s

def check_membership(s: set, value: str) -> bool:
    return value.isdigit() and int(value) in s

s = {1, 2, 3, 'a', 'e', 'i', 'o', 'u', "red", "green", "blue"}
value = "2"
print(check_membership(s, value))