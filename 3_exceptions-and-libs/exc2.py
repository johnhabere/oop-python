try:
    x = int(input("Enter x: ")) # x will not be created if it isn't any integer
except ValueError:
    print("Oops x isn't an Integer")
else:
    print(f"You entered {x}")