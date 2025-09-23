def num_to_text(num):
    result, num, n = "", str(num), 0
    for i in num:
        if i == "0" : result += "ZERO "
        elif i == "1" : result += "ONE "
        elif i == "2" : result += "TWO "
        elif i == "3" : result += "THREE "
        elif i == "4" : result += "FOUR "
        elif i == "5" : result += "FIVE "
        elif i == "6" : result += "SIX "
        elif i == "7" : result += "SEVEN "
        elif i == "8" : result += "EIGHT "
        elif i == "9" : result += "NINE "
    return result

print(num_to_text(638342))

# def num_to_text(num):
#     result, num, n = "", str(num), 0
#     for i in num:
#         if i == "0" : result += "ZERO "
#         elif i == "1" : result += "ONE "
#         elif i == "2" : result += "TWO "
#         elif i == "3" : result += "THREE "
#         elif i == "4" : result += "FOUR "
#         elif i == "5" : result += "FIVE "
#         elif i == "6" : result += "SIX "
#         elif i == "7" : result += "SEVEN "
#         elif i == "8" : result += "EIGHT "
#         elif i == "9" : result += "NINE "
#     return result.rstrip()
#
# print(num_to_text(638342))
#
# def num_to_text(num):
#     text = {0:"ZERO ",1:"ONE ",2:"TWO ",3:"THREE ",4:"FOUR ",5:"FIVE ",6:"SIX ",7:"SEVEN ",8:"EIGHT ",9:"NINE "}
#     result = ""
#     for i in str(num):
#         if int(i) in text: result +=  text[int(i)]
#     return result.rstrip()
# print(num_to_text(638342))