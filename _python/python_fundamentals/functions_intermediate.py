import random

def randInt(min= 0, max= 100):
    if min > max:
        return "min must be smaller than max!"
    else:
        max = max-min;
        num = round(random.random() * max + min)
        return num
print(randInt())
print(randInt(-10, -5))
print(randInt(90))
print(randInt(max = 10))
print(randInt(10,5))



# print(randInt())    # should print a random integer between 0 to 100
# print(randInt(max=50))  # should print a random integer between 0 to 50
# print(randInt(min=50))  # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500



