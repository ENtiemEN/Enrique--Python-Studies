import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# Row selection
# array[start:end:step] # end is EXCLUSIVE
print(array[:-1:2], end='\n\n')

print(array[::-1], end='\n\n')

print(array[::-2], end='\n\n')

# Column selection
print(array[:,-1], end='\n\n')
print(array[-1,-1], end='\n\n')

# Row and Column selection
print(array[1:3,1:3],end='\n\n')

# Work -> Sum all the columns
sum_cols = 0
for i in range(4):
  sum_cols += array[:,i]

print(f"Sum of the columns -> {sum_cols}")
print(f"Shape of the result -> {sum_cols.shape}")

# Work -> Summ all the rows
sum_rows = 0
for i in range(4):
  sum_rows += array[i,:]

print(f"Sum of the rows -> {sum_rows}")
print(f"Shape of the result -> {sum_rows.shape}")

# Mirror my `ndim=2` numpy array
# Mirror by rows
print(f"Mirror matrix (by row) ->\n{array[::-1,:]}")

# Mirror by columns
print(f"Mirror matrix (by column) ->\n{array[:,::-1]}")
