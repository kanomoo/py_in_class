name = input("name : ") # input somchai
re = name[::-1]
mess = "\n"
for i in range(len(name)):
    mess += (" " * i + re[i:])
    mess += f"{name[1:len(name) - i]}\n"
print(mess)

name = input("name : ") # input somchai
re = name[::-1]
mess = "\n"
for i in range(len(name)):
    mess += (" " * (len(name)- i-1) + re[-(i+1):])
    mess += f"{name[1:i+1]}\n"
print(mess)

name = input("name : ") # input python
mess = "\n"
for i in range(len(name)):
    mess += (" " * (len(name) - i-1))
    for n in name[:i+1]:
        n = f"{n} "
        mess += n
    mess += "\n"
print(mess)

name = input("name : ")
mess = "\n"
for i in range(len(name)):
    mess += " " * i
    for n in name[:len(name) - i]:
        mess += f"{n} "
    mess += "\n"
print(mess)
