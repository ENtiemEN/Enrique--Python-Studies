import numpy as np

array = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])

print(f"Array to work with:\n{array}")
print(f"Sum -> {np.sum(array)}")
print(f"Mean -> {np.mean(array)}")
print(f"Standard deviation -> {np.std(array)}")
print(f"Variance -> {np.var(array)}")
print(f"Min -> {np.min(array)}. In the index [{np.argmin(array)}]")
print(f"Max -> {np.max(array)}. In the index [{np.argmax(array)}]")

print(array[1][-2])
#print(array[9])
