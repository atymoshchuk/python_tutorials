import time


# decorator to have function's timing
def timeit(method):
    def timed(*args, **kw):
        # saving time before execution
        ts = time.time()
        result = method(*args, **kw)
        # saving time after execution
        te = time.time()
        # printing function's timing
        print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts))
        # returning function's result
        return result
    return timed

# let's see how can we reuse timing decorator for different functions


class Foo(object):

    # decorate class' function
    @timeit
    def foo(self):
        time.sleep(0.2)
        print('foo from class Foo')


# decorate function without arguments
@timeit
def f1():
    time.sleep(1)
    print('f1')


# decorate function with arguments
@timeit
def f2(a):
    time.sleep(2)
    print('f2', a)


# decorate function with args and kwargs
@timeit
def f3(*args, **kw):
    time.sleep(0.3)
    print('f3', args, kw)


# check how it works
f1()
f2(42)
f3(42, 43, foo=2)
Foo().foo()
