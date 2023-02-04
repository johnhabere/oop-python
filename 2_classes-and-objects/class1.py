class Rolex:
    
    def __init__(self):
        pass
    # attributes
    chapati_size: str
    number_of_eggs: int
    withSalt: bool
    toppings: bool

    def price(self, tax):
        total =0.0
        if self.chapati_size == "large":
            total = total + 3000
        elif self.chapati_size == "medium":
            total = total + 2000
        else:
            total = total + 1000
        
        total = total + self.number_of_eggs * 500
        
        if self.toppings:
            total = total + 1000
        
        total = total * tax
        
        return total

a_rolex: Rolex = Rolex()
a_rolex.chapati_size = "large"
a_rolex.number_of_eggs = 3
a_rolex.withSalt = True
a_rolex.toppings = False


print(a_rolex.price(1.18))
# print(a_rolex)
# print(a_rolex.chapati_size)

