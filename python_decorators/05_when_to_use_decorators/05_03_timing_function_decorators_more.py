import time


# decorator to have function's timing
def timeit(method):
    # ts = time.time()
    # time.sleep(1)
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


# decorate function without arguments
@timeit
def f1():
    time.sleep(1)
    print('f1')


# check how it works
f1()
# f1()
