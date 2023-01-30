class HallAllocationError(Exception):
    pass

class HomeDistanceError(Exception):
    pass

def checkHomeDist(distance):
    maxDistance = 80
    if distance < maxDistance:
        raise HomeDistanceError("You can commute from home")
    else:
        print("You may be allocated a hall")

def checkAge(age):
    ageLimit = 30
    if age > ageLimit:
        raise HallAllocationError("You are too old to be allocated a hall")
    else:
        dist = int(input("Distance = "))
        checkHomeDist(dist)
    
try:
    age = int(input("What is your age?"))
    checkAge(age)
except HallAllocationError as haErr:
    print(haErr)
except HomeDistanceError as hoErr:
    print(hoErr)