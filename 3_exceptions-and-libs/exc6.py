num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))

if num2 == 0:
    raise ZeroDivisionError("No division by zero")
else:
    print("Quotient =",num1/num2)