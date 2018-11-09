def multipliers():
    return [lambda x: i * x for i in range(4)]


# don't run the code, think first what would you expect to be printed?
print([m(2) for m in multipliers()])
