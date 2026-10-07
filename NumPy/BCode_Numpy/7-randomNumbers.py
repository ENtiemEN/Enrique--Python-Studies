import numpy as np




# Integer numbers ==========================

## Obs -> We can set a seed (If you don't, Python will set it for you)

rng = np.random.default_rng(seed=1)
print(rng.integers(1, 7)) # <- Second numbers is exclusive (as in `range`)

## For redability, we can use keyword arguments

print(rng.integers(low=1, high=7))

## We can set a size, or amount of random numbers we want

print(rng.integers(low=1,high=7, size=3))

## With `size` keyword argument We can change the shape

print(rng.integers(low=1,high=7, size=(4,2)))

# Decimal numbers ==========================

## Set a seed
np.random.seed(seed=1)

print(np.random.uniform(low=-1, high=1, size=(3,1)))

# ==========================================
# Shuffle an array

rng2 = np.random.default_rng()

array = np.array([1,2,3,4,5])

rng2.shuffle(array)

print(array)

# Random Selections ==========================
print('\n')

fruits = np.array(["apple","orange","banana","coconut","pineapple"])
print(type(fruits))

fruits = rng2.choice(fruits, size=(3,3))
print(fruits)

print(type(fruits))


