def dec(f):
    def wrapper(*argv):
        print('Arguments got:', argv, 'Decorated!')
        return f(*argv)
    return wrapper


def f(n):
    print(n, 'Original!')
    if n == 1:
        return 1
    else:
        return f(n - 1) + n


print("first example - original function")
print(f(5))

dec_f = dec(f)
print("second example")
print(dec_f(5))

f = dec(f)
print("third example")
print(f(5))
