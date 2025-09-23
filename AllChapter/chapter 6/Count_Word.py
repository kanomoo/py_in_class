while True:
    name = input("Enter text(space to next word 'exit to exit') : ")
    if name == "exit": break
    a_word = ""
    for i in name.split():
        if i not in a_word : 
            a_word += i
            print(f"{i} count = {name.count(i)}")
    print()