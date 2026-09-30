import numpy as np
'''
Broadcasting allows NumPy to perform operations on arrays
with different shapes by virtually expanding dimensions
so they match the larger array's shape.

(Conditions - 'for the colums'. Think like zip)
The dimensions have the same size
OR
One of the dimensions has a size of 1
e.g: (1,4) + (4,1)


e.g ->
a(4x3) + b(1x3) = result(4x3)
O O O    O O O    O O O
O O O    _ _ _    O O O
O O O    _ _ _    O O O
O O O    _ _ _    O O O
'''

array1 = np.array([[1,2,3,4]]) # ndim=1 , shape=(1,4)
array2 = np.array([[1],[2],[3],[4]]) #ndim=2 , shape=(4,1)
print(f"Array1:\n {array1}\nShape: {array1.shape}")
print(f"Array2:\n {array2}\nShape: {array2.shape}")

print(f"Broadcasting (+ and *)")
print(array1 + array2)
print(array1 * array2)
''' The result from
00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33
'''

array1 = np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]]) # shape = (4,4)

array2 = np.array([[1],[2],[3],[4]]) # shape = (4,1)

print(f"\nArray1:\n {array1}\nShape: {array1.shape}")
print(f"Array2:\n {array2}\nShape: {array2.shape}")

print(f"Broadcasting (+):\n{array1+array2}")

print("\n= = = = = = = = = = = = = = = = = = =\n")

print("Times table")
array1 = np.array([[1,2,3,4,5,6,7,8,9,10,11,12]]) # shape=(1,12)
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]]) # shape=(12,1)

total = array1 * array2
#print(total) # shape(12,12)

userInput = int(input("Choose a #n times table chart (1-12): "))

# Multiplication table
for i,n in enumerate(total[userInput-1]):
  print(f"{userInput}x{i+1}={n}")
