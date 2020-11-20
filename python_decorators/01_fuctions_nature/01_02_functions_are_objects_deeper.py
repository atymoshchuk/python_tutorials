def say_hello(name):
    # let's use the same simple function as in an example above
    print("Hello %s!" % name)


# call the function with argument
say_hello("Conference")

# assign function as a FCO (first-class object) to a variable
my_func = say_hello

# call the function, should do exactly the same as calling the original
# function, as it's pointing to the same function
my_func("Awesome Conference")

# delete say_hello variable, not a function!
del say_hello

# call the function with the other argument, should still work as it's pointing
# to the same original function, although the variable <say_hello> was removed
my_func("Team")

# just to be sure that the function is still the same
print(my_func.__name__)

# this line will throw NameError exception, as we removed <say_hello>
say_hello("just somebody")
