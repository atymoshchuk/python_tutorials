"""
Found on stackoverflow some weird example, let's see what's wrong here
"""


# simple decorator
def dec(f):
    def wrapper(*argv):
        print('Arguments got:', argv, 'Decorated!')
        return f(*argv)
    return wrapper


# simple function
def f(n):
    print(n, 'Original!')
    if n == 1:
        return 1
    else:
        return f(n - 1) + n


print("first example - original function")
# call simple function with parameter
print(f(5))


# wrong usage of decorator, it's not equal to "@dec" and to f=dec(f)
dec_f = dec(f)
print("second example")
print(dec_f(5))

f = dec(f)
print("third example")
print(f(5))
