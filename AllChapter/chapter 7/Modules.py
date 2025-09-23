def sum_number(start = 1, end = 10):
    sum = 0
    for n in range(start, end+1):
        sum += n
    return(sum)

def factorial(num):
    if num > 0: return (num * factorial(num - 1))
    else: return(1)

def draw_triangle(ch,num):
    for n in range(1, num+1):
        print(ch * n)