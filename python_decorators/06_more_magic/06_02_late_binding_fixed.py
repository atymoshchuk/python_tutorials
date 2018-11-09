def multipliers():
    """
    if you will not bind i, then the result will be
    The output of the above code will be [6, 6, 6, 6] (not [0, 2, 4, 6])

    The reason of it is late binding.
    It means that the values of variables used in closures are looked up
    at the time the inner function is called.

    You can read more here:
    Common Gotchas — The Hitchhiker's Guide to Python
        https://docs.python-guide.org/writing/gotchas/
    """
    return [lambda x, i=i: i * x for i in range(4)]


print([m(2) for m in multipliers()])
