## Create your custom exceptions
# - clean code
# - documentation
# - set yourself away from others

class AgeErrorException(Exception): # inheritance
    def __init__(self, value):
        self.value = value

try:
    age = int(input("What is your age?:"))
    if age < 0 or age >=80:
        raise AgeErrorException("Out of range age")
    print(f"You are {age} years OLD")
except ValueError:
    print("We accept only integers")
except AgeErrorException as ageErr:
    print(ageErr)