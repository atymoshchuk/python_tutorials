import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts))
        return result

    return timed


class Foo(object):

    @timeit
    def foo(self):
        time.sleep(0.2)
        print('foo from class Foo')


@timeit
def f1():
    time.sleep(1)
    print('f1')


@timeit
def f2(a):
    time.sleep(2)
    print('f2', a)


@timeit
def f3(*args, **kw):
    time.sleep(0.3)
    print('f3', args, kw)


f1()
f2(42)
f3(42, 43, foo=2)
Foo().foo()
