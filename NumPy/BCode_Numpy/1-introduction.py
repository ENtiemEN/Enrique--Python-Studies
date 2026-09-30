import numpy as np

#print(np.__version__)

my_list = [1,2,3,4]
my_list = my_list*2 # [1,2,3,4,1,2,3,4] (Concatenation)
print(f"Python List: {my_list} Type: {type(my_list)}")

array_2d = np.array([[1,2,3,], [4,5,6], [7,8,9]])

array_3d = np.array([[['A','B'],['C','D']],
                     [['E','F'],['G','H']],
                     [['I','J'],['K','L']]])

print(f"Dimensión del 2d array -> {array_2d.ndim}")
print(f"Shape del 2d array -> {array_2d.shape}") # (rows, cols)
print(f"Numpy Array: {array_2d} Type: {type(array_2d)}")

print(f"Dimensión del 3d arrat -> {array_3d.ndim}")
print(f"Shape del 3d array -> {array_3d.shape}") # (depth, rows, cols)

print("\n= = = = = = = = = = = = = = = = = = =\n")

# Chain indexing
print(array_3d[1][1][1]) # H

# Multidimensional indexing (Is faster than chain indexing)
print(array_3d[1,1,1])

# Form a word using string concatenation
word = array_3d[0,1,0]+array_3d[0,0,0]+array_3d[2,1,1]+array_3d[1,0,0]+array_3d[0,0,1]
print(word) # CALEB
