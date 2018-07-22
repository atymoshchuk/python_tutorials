def first_dec(func):
    def wrapped(*args, **kwargs):
        print("Something happened in First decorator!")
        return func(*args, **kwargs)

    return wrapped


def second_dec(func):
    def wrapped(*args, **kwargs):
        print("Something happened in Second decorator!")
        return func(*args, **kwargs)

    return wrapped


@first_dec
@second_dec
def myfunc(myarg):
    print("my function", myarg)


def mysecond_func(myarg):
    print("my second function", myarg)


myfunc('for the Talk')
mysecond_func = first_dec(second_dec(mysecond_func))
mysecond_func('is doing the same')
