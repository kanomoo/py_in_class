try:
    num1 = int(input("Enter value number1 : "))
    num2 = int(input("Enter value number2 : "))
    print("number1 + number2 = " , num1+num2)
    print("number1 - number2 = " , num1-num2)
    print("number1 * number2 = " , num1*num2)
    print("number1 / number2 = " , num1/num2)
except ValueError:
    print("You input datain correct, input again.")
except ZeroDivisionError:
    print("Number is not divide with zero.")
except NameError:
    print("Use varibable not defind.")
except:
    print("Error in program.")
print("This is test Exception.")