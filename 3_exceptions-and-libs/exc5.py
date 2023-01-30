
# try ... except .... else ... finally

try:
    nume = int(input("Enter the numerator: "))
    denom = int(input("Enter the denominator: "))
    quotient = nume/denom
    print("Correct division")
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Only integers required")
else:
    print("Quotient =", quotient)
finally:
    print("I am always here")