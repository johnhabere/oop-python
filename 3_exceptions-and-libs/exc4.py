def main():
    z = get_int()
    print(f"You entered {z}")

def get_int():
    while True:
        try:
            return int(input("Enter x: ")) # x will not be created if it isn't an integer
        except ValueError:
            print("Oops x isn't an Integer")

main()