# def factorial1(number):
#     fac = 1
#     for n in range(1, number+1):
#         fac = fac * n
#     return(fac)
#
# def factorial2(number):
#     if number > 0:
#         return(number * factorial2(number - 1))
#     else:
#         return(1)
#
# num = int(input("Enter number : "))
# print("Factorial1 with for = ", factorial1(num))
# print("Factorial2 with recursive = ", factorial2(num))









# def factorial1(number): # n! = 1...*n
#     fac = 1
#     for n in range(1, number+1):
#         fac *= n 
#     return(fac)

# def fac2(number): #n! = n * (n-1)!
#     if number > 0: return   number * fac2(number-1)
#     else: return(1)

# def fac3(num):
#     if num > 0: return num * fac3(num-1)
#     else: return(1)

# def ff1(num):
#     fac = 1
#     for i in range(1,num+1):
#         fac *= i
#     return fac

# def ff2(num):
#     if num >0 : return num * ff2(num-1)
#     else: return 1


# num = 5
# print(factorial1(num))
# print(fac2(num))
# print(fac3(num))
# print(ff1(num))
# print(ff2(num))


def fac1(number): # n! = 1 x 2 x 3 x 4 x 5 x ... x n
    fac = 1
    for  i in range(1, number+1):
        fac *= i
    return fac

def fac2(number): # n! = n x (n-1)!
    if number > 0: return(number * fac2(number - 1))
    else: return 1


number = int(input("Enter number : "))
print(f"Factorial1 with for = {fac1(number)}")
print(f"Factorial2 with for = {fac2(number)}")