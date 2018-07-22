from functools import wraps


def mydecorator(f):
    @wraps(f)
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
