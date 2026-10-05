def firstDecorator(function):
    def wrapper():
        print("I'm your 1st decorator function")
        function()

    return wrapper

def hello_world():
    print("Hello World!")

# # wra = myDecorator(hello_world)
# # wra()
#firstDecorator(hello_world)()

# ==============================================

# In python the syntax is different
def secondDecorator(function):
    def wrapper():
        print("I'm your 2nd decorator function")
        function()

    return wrapper

@secondDecorator
def bye_world():
    print("Bye World!")

#bye_world()

# ==============================================

def mydecorator(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("I'm your decorator function")
        return return_value

    return wrapper

@mydecorator
def hello(person):
    return f"Hello {person}!"

#print(hello("MIKE"))

# ==============================================
# Practical Example #1 -- Logging

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logged
def add(x,y):
    return x+y

#add(10,20)

# ==============================================
# Practical Example #2 -- Timed
import time

## Esta versión no tiene en cuenta una implementación recursiva
'''
def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute")
        print(f"{fname} result -> {value}")
        return value
    return wrapper
'''
def timed(function):
    depth = 0
    t_start = 0
    def wrapper(*args, **kwargs):
        nonlocal depth, t_start
        # Registramos el tiempo en la primera llamada
        if depth == 0:
            t_start = time.time()
        depth +=1

        try:
            value = function(*args, **kwargs)
        finally:
            depth -= 1

        # Solo imprimimos cuando todas las llamadas recursivas terminaron
        if depth == 0:
            total_time = time.time() - t_start
            fname = function.__name__
            print(f"{fname} took {total_time} seconds to execute")
            #print(f"{fname} result -> {value}")
        return value
    return wrapper

@timed
def factorialRecursive(n):
    if n<=1:
        return 1
    return n * factorialRecursive(n-1)

@timed
def factorialIterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

factorialIterative(900000)
#factorialRecursive(90)