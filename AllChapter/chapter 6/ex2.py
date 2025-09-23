while True:
    name = input("Enter text(enter-exit) : ")
    if name == "": break
    elif name.isalpha(): print("Text is alphabetic")
    elif name.isdigit(): print("Text is isdigit")
    elif name.isalnum(): print("Text is alpha and numeric")
    elif type(name) == str and name != "" and name != " ": print("Text is string")    