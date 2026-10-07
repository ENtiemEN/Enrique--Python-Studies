'''
  Filtering -> Refers to the process of selecting elements from an array that match a given condition
'''
import numpy as np

ages = np.array([[18,17,19,20,14,90,20,21],
                 [65,40,17,19,22,21,23,24]])

teenagers = ages[ages < 18]
adults = ages[(ages>=18) & (ages<65)] # <- NumPy uses C style array
seniors = ages[ages>=65]

even_ages = ages[ages % 2 == 0]

## The results are flattened -> 1D
print(seniors)
print(even_ages)


''' `.where()` -> preserves the form

`where(condition,x,y)` : Select x if True, and y if False.
`condition`,'x','y' must be broadcastable to a common shape

Using `.where()` is more slow than using boolean indexing
'''

adults = np.where(ages >= 18, ages, 0)

## Return the original shape, and the elements who don't match thecondition are replaced by 0
print(adults)
print(f"Shape -> {adults.shape}, Dimension -> {adults.ndim}")

