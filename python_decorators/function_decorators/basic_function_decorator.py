def mydecorator(decorated_func):
    def wrapped(*args, **kwargs):
        print("Something happened in decorator!")
        return decorated_func(*args, **kwargs)

    return wrapped


@mydecorator
def myfunc(myarg):
    print("my function", myarg)


def mysecond_func(myarg):
    print("my second function", myarg)


myfunc('for the Talk')
mysecond_func = mydecorator(mysecond_func)
mysecond_func('is doing the same')
