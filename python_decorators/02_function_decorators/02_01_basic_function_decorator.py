# let's create a simple decorator
def mydecorator(decorated_func):
    def wrapped(*args, **kwargs):
        # decorator will print the phrase
        print("Something happened in decorator!")

        # and return result of the function back,
        # without of modifying it's behaviour
        return decorated_func(*args, **kwargs)
    return wrapped


# let's use decorator with syntactic sugar "@"
@mydecorator
def myfunc(myarg):
    print("my function", myarg)


# just simple function
def mysecond_func(myarg):
    print("my second function", myarg)


# calling the first decorated function
myfunc('for the Talk')

# let's decorate the second function with the same decorator,
# but without using syntactic sugar;
# it's identical with the first example with "@"
mysecond_func = mydecorator(mysecond_func)

# run the code and make sure that it works in the same way
mysecond_func('is doing the same')
