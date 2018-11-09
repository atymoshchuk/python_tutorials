# simple decorator without parameters
def mydecorator(decorated_func):
    def wrapped(*args, **kwargs):
        print("Before decorated function")
        # result can be modified after function is called,
        # before return from decorator
        result = decorated_func(*args, **kwargs)
        print("After decorated function")
        return result
    return wrapped


# use mydecorator with syntactic sugar "@"
@mydecorator
def myfunc(myarg):
    """prints some text combined with a string from argument"""
    print("my function", myarg)
    return "return value"


# call the function and store it's result in "r" variable to use it later
r = myfunc('for the Talk')

# print function's name after it was decorated
print("My func name is:", myfunc.__name__)

# print function's docstring after it was decorated
print("My func docstring is:", myfunc.__doc__)

# After you run the example.. there is something weird happening:
# docstring is empty and name of the function is the name of the wrapper,
# which will make a confusion and misunderstanding in the future.
# How to fix it? See the next example.
print(r)
