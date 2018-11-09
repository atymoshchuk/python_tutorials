"""
Basic class decorator will look like:

class my_decorator:
    ....
    # probably a lot of code here

@my_decorator
class MyClass:
    def do_something(self):
        ...

Here is an example of using a class as a decorator

"""


# create simple class which has __init_ and __call__ functions redefined
# the goal is to print to the terminal when we entered the function
# and print it's name
class entry_exit(object):

    def __init__(self, f):
        # __init__ is a special method in Python classes,
        # it is the constructor method for a class.
        self.f = f

    def __call__(self):
        # the __call__ method is called when the instance is called
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)


# use class decorator with syntactic sugar "@", decorate func1
@entry_exit
def func1():
    print("inside func1()")


# use class decorator with syntactic sugar "@", decorate func2
@entry_exit
def func2():
    print("inside func2()")


# call decorated functions
func1()
func2()
