'''
    Generators have something called LAZY EXECUTION
    e.g in Haskell -> [2,...,90]
'''
import sys

def myGenerator(n):
    for x in range(n):
        yield x

values = myGenerator(100)
#print(sys.getsizeof(values))
#print(next(values))
#print(next(values))
#print(list(values))

# for x in values:
#     print(x)

# ===========================================================

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()
# print(next(values))
# print(next(values))
for _ in range(10):
    print(next(values), end=" ")

