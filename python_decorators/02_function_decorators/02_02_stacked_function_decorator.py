# first simple decorator
def first_dec(func):
    def wrapped(*args, **kwargs):
        print("Something happened in First decorator!")
        return func(*args, **kwargs)

    return wrapped


# second simple decorator
def second_dec(func):
    def wrapped(*args, **kwargs):
        print("Something happened in Second decorator!")
        return func(*args, **kwargs)

    return wrapped


# example how to use stacked decorators with syntactic sugar
@first_dec
@second_dec
def myfunc(myarg):
    print("my function", myarg)


# just simple function
def mysecond_func(myarg):
    print("my second function", myarg)


# call the first decorated function
myfunc('for the Talk')

# let's decorate the second function in more visible way to understand
# how it works, it's identical to the previous example with "@"
mysecond_func = first_dec(second_dec(mysecond_func))

# call the second decorated function, which works in the same way as first
mysecond_func('is doing the same')
