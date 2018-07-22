def time_this(original_function):
    print("decorating")

    def new_function(*args, **kwargs):
        print("starting timer")
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time = {0}".format(after - before))
        return x

    return new_function


def time_all_class_methods(Cls):
    class NewCls(object):
        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__):  # it is an instance method
                return time_this(x)  # this is equivalent of just decorating the method with time_this
            else:
                return x

    return NewCls


# now lets make a dummy class to test it out on:

@time_all_class_methods
class Foo(object):
    def a(self):
        print("entering a")
        import time
        time.sleep(3)
        print("exiting a")

    def b(self):
        print("entering b")
        import time
        time.sleep(0.5)
        print("exiting b")

    def c(self):
        print("entering c")
        import time
        time.sleep(0.9)
        print("exiting c")


oF = Foo()
oF.a()
oF.b()
oF.c()
