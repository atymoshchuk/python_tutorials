def mydecorator(decorated_func):
    def wrapped(*args, **kwargs):
        print("Something happened in decorator!")
        return decorated_func(*args, **kwargs)
    return wrapped


@mydecorator
def myfunc(myarg):
    print("my function", myarg)


@mydecorator
def recursive_func(n):
    print("Original function")
    if n == 0:
        return 0
    return n + recursive_func(n - 1)


recursive_func(10)
