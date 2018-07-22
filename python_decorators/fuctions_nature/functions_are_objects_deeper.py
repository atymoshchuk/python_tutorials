def say_hello(name):
    print("Hello %s!" % name)


say_hello("EuroPython 2018")

my_func = say_hello

my_func("Awesome EuroPython 2018")
del say_hello

my_func("Team")
print(my_func.__name__)
say_hello("just somebody")
