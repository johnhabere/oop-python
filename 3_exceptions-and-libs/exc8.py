## Create your custom exceptions
# - clean code
# - documentation
# - set yourself away from others

class AgeErrorException(Exception): # inheritance
    def __init__(self, value, message="Age out of range"):
        self.value = value
        self.message = message
        super().__init__(self.message)

age = int(input("What is your age? "))
if not 0 < age < 80:
    raise AgeErrorException(age)