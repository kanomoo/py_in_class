# while True:
#     name = input("Enter text(enter-exit) : ").lower()
#     if name == "exit": break
#     print(f"Text has 'a' : {name.count("a")}")
#     print(f"Text has 'e' : {name.count("e")}")
#     print(f"Text has 'i' : {name.count("i")}")
#     print(f"Text has 'o' : {name.count("o")}")
#     print(f"Text has 'u' : {name.count("u")}\n")


while True:
    name = input("Enter text(enter-exit) : ")
    if name == "": break
    print(f"Text has 'a' : {name.lower().count("a")}")
    print(f"Text has 'e' : {name.lower().count("e")}")
    print(f"Text has 'i' : {name.lower().count("i")}")
    print(f"Text has 'o' : {name.lower().count("o")}")
    print(f"Text has 'u' : {name.lower().count("u")}\n")