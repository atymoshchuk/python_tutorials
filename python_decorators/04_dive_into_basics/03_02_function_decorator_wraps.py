from functools import wraps


def mydecorator(f):
    @wraps(f)
    # This is a convenience function for invoking update_wrapper() as
    #  a function decorator when defining a wrapper function.
    # It is equivalent to
    # partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)
    # More information: https://docs.python.org/3.7/library/functools.html
    # It will actually fix the previous issue with wrong function's name
    # and docstring. Advice: always use functools.wraps decorator.
    def wrapped(*args, **kwargs):
        print("Before decorated function")
        r = f(*args, **kwargs)
        print("After decorated function")
        return r
    return wrapped


@mydecorator
def myfunc(myarg):
    """prints some text combined with a string from argument"""
    print("my function", myarg)
    return "return value"


r = myfunc('for the Talk')
print("My func name is:", myfunc.__name__)
print("My func docstring is:", myfunc.__doc__)
print(r)
