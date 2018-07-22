def mydecorator(decorated_func):
    def wrapped(*args, **kwargs):
        print("Before decorated function")
        result = decorated_func(*args, **kwargs)
        print("After decorated function")
        return result
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
