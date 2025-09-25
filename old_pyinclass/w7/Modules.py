def sum_number(start = 1, end = 10):
    sum = 0
    for n in range(start, end + 1):
        sum += n
    return(sum)

def factorial(num):
    if num > 1:
        return(num *  factorial(num - 1))
    else:
        return(1)

def draw_triangle(ch, num):
    for n in range(1, num +1):
        print(ch * n)


#ทำ เอง
# def sum():
#     sum = 0
#     start = int(input("Start : "))
#     end = int(input("End : "))
#     for i in range(start, end+1):
#         sum += i
#     print(f"\nSum {start} - {end} = {sum}\n")
#
#
# def factorial():
#     n = int(input("N : "))
#     fac = 1
#     for i in range(1, n + 1):
#         fac = i * fac
#     print(f"\nFactorial = {fac}\n")
#
# def triangle():
#     ch = input("Ch : ")
#     num = int(input("Num : "))
#     print()
#     for i in range(1,num+1):
#         print(str(ch) * i)
#     print()