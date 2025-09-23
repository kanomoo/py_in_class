# import math
# print("Equation 1 : sin x ^2 + cos x ^ 2")
# x = float(input("Enter value x (degree angle) : "))
# print("x =",x) #56.4
# print("value of sin x ^2 + cos x ^ 2 is",format(pow(math.sin(x),2) + pow(math.cos(x),2),".8f")) #ต้อง format เพื่อให้มีทศนิยม 8 ตำแหน่ง

# print("\nEquation 2 : e^(0.5 sqrt( tan cos x ) )")
# x = float(input("Enter value x (degree angle <= 90) : "))
# print("x =",x) # 23.7
# x = math.radians(x) # math.cos tan ต้องการค่ามุมในหน่วยเรเดียน radians
# print("value of   e^(0.5 sqrt( tan cos x ) ) is",math.exp(1/2 * math.sqrt(math.tan(math.cos(x)))))

# print("\nEquation 3 : [ log(x^2/(1-x)) ] / [ x^(5+x) ]")
# x = float(input("Enter value x (0.0 - 1.0 ) : "))
# print("x =",x) # 0.345  #log ธรรมดาเป็นฐาน e natural logarithm  ต้องใช้ log ฐาน 10
# print("value of [ log(x^2/(1-x)) ] / [ x^(5+x) ] is",math.log10(pow(x,2) / (1-x)) / (pow(x,5+x)))

# import math as m
# x = float(input("ETner angle : "))
# x = m.radians(x)
# print(pow(m.sin(x),2) * pow(m.cos(x),2))
# print(m.exp(1/2 * m.sqrt(m.tan(m.cos(x)))))
# print(m.log10(pow(x,2)/(1-x)) / pow(x,5+x))

# import math as m
# x = float(input("Enter angle : "))
# rad = m.radians(x)
# eq1 = pow(m.sin(rad),2) * pow(m.cos(rad),2)
# print("Eq1 = ", eq1)

# import math as m 
# x = float(input("Enter angle : "))
# rad = m.radians(x)
# eq2 = m.exp(0.5 * m.sqrt(m.tan(m.cos(rad))))
# print("Eq2 = ", eq2)

from math import log10
x = float(input("Enter float number : "))
eq3 = log10(pow(x,2) / (1-x) / pow(x,5+x))
print("Eq3 : ", eq3)