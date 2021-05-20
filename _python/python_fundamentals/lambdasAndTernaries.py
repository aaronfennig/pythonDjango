# EXAMPLE OF TERNARY OPERATORS IN PYTHON

stacks = 2
print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')


#  LAMBDA FUNCTIONS

# Earlier, we defined the square() function that takes in one parameter (num), squares it and then returns it:

# def square(num):
#     x = num ** 2
#     return x
# copy
# Now we can rewrite this function as an anonymous (nameless) lambda function:

# lambda num: num ** 2


# define a function that takes one input that is a function
def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(2))


invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)


# create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x: x ** 2]
# access the value in the list
print(my_list[2])  # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
print(my_list[2](5))


def add10(x): return x + 10  # store lambda expression in a variable


add10(2)  # returns 12
add10(98)  # returns 108


# create a list
my_arr = [1, 2, 3, 4, 5]
# define a function that squares values


def square(num):
    return num ** 2


# invoke map function
print(list(map(square, my_arr)))

# ABOVE IS SAME AS BELOW

my_arr = [1, 2, 3, 4, 5]
# invoke map, pass in a lambda as the first argument
print(list(map(lambda x: x ** 2, my_arr)))
