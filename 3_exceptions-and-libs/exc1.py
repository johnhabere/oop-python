try:
    x = int(input("Enter x: "))
    print(f"You entered {x}")
except ValueError:
    print("Oops x isn't an Integer")