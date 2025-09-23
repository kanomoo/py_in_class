# print(" #####  #####  #       #      #\n #	#   	#     # #    #\n ####	#####	 #   #  #   #\n # 	#    	 # ##	  ##\n # 	#####	  ##	  ##\n")

# x = 5
# print(type(x))
# y = "John"
# x = str(x)
# print(x)
# print(y)

# x = 3.14
# x = int(x)
# print(x)

# input number1
# input number2
# number1 + number2 = result
# display result

######################################################
# input age
# age = age + 10
# display age

# age = int(input("age: "))
# print(age + 10)
# score = 60
# if score >= 50:
#     print("Pass\n")

# name = "Paphavin"
# if name == "Paphavin":
#     print(f"You name is {name}")
print()
###################################################
while True:
    c1 = int(input("Player 1 - Choose your move:\n1 = Rock\n2 = Paper\n3 = Scissors\nEnter 1, 2, or 3: "))
    c2 = int(input("\nPlayer 2 - Choose your move:\n1 = Rock\n2 = Paper\n3 = Scissors\nEnter 1, 2, or 3: "))

    g = {1:"Rock",2:"Paper",3:"Scissors"}
    for i in g:
        if c1 == i: r1 = g[i]
        if c2 == i: r2 = g[i]

    if c1 >3 and c2 >3 : result = "Invalid input! Please enter 1, 2, or 3 only."
    elif c1 == c2: result = "It's a tie!"
    elif c1 > c2: 
        result = "Player 1 wins!"
        if c2 == 1 and c1 == 3: result = "Player 2 wins!"
    elif c2 > c1: 
        result = "Player 2 wins!"
        if c1 == 1 and c2 == 3: result = "Player 1 wins!"

    print(f"\nPlayer 1 chose: {r1}\nPlayer 2 chose: {r2}\n{result}")
    print("====================")