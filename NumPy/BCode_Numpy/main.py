import numpy as np

#print(np.__version__)

my_list = [1,2,3,4]

my_list = my_list*2 # [1,2,3,4,1,2,3,4] (Concatenation)

print(f"List: {my_list} Type: {type(my_list)}")

array = np.array([1,2,3,4])

array = array * 2

print(f"Numpy Array: {array} Type: {type(array)}")
