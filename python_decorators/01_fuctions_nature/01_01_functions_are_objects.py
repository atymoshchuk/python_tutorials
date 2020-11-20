"""
All functions in Python are first class objects (FCO)
It means that all of them has all the properties of FCO:
- can assign to variables;
- store FCO in data structures;
- pass FCO as arguments to other functions;
- return FCO as a value from other function.

It's a key to understanding how decorators can work
"""


def say_hello(name):
    # simple function which will print something to the screen
    print("Hello %s!" % name)


# call the function with argument
say_hello("Conference")

# assign function as a FCO to a variable
my_func = say_hello

# call the function, should do exactly the same as calling the original
# function, as it's pointing to the same function
my_func("Awesome Conference")
