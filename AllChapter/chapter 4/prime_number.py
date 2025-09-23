from math import gcd 
while True:
    num = int(input())
    if gcd(num) == num: print("prime")
    else: print("not prime")