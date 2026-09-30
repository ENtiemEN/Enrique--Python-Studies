import numpy as np

# SCALAR ARITHMETIC
array = np.array([1,2,3.99])
print(f"Numpy Array -> {array}")

answer = str(input("Want Scalar arithmetich? (y/n) "))
flag = True if 'y'==answer else False
if flag:
  opt = str(input('Enter the operation (+,-,*,/,^): '))
  scalar = float(input('Enter the scalar: '))
  match opt:
    case '+':
      print(array + scalar)
    case '-':
      print(array - scalar)
    case '*':
      print(array * scalar)
    case '/':
      print(array / scalar)
    case '^':
      print(array ** scalar)
    case _:
      print("Operador inválido")

# VECTORIZED MATH FUNCTIONS
print(f"Sqrt func:\n {np.sqrt(array)}")
print(f"Round func:\n {np.round(array)}")
print(f"Floor func:\n {np.floor(array)}")
print(f"Ceil func:\n {np.ceil(array)}")

# ELEMENT-WISE ARITHMETIC

## e.g. Maintenance Calories (TDEE) for 3 man
## TDEE <> Total Daily Energy Expenditure:
## TDEE = BMR X Activity Multiplier
## Sedentary: 1.2, Lightly act: 1.375, Moderately act: 1.55, Very active: 1.724, Extra active: 1.9
weight_kg = np.array([81,90,71])
height_cm = np.array([174, 191, 182])
age = np.array([23, 20, 19])
activity_multiplier = np.array([1.375, 1.2, 1.724])

BMR = (10*weight_kg) + (6.25*height_cm) - (5*age)
print(f"Caloric maintenance:\n {BMR * activity_multiplier}")

# COMPARISON OPERATORS
scores = np.array([91, 55, 100, 73, 82, 62])
print(f"\nMy array the scores are -> {scores}")

#print(scores == 100)
print(f"Scores different form 100 -> {scores[scores != 100]}")
## Filtering
print("Replacing the scores less than 100 for 0:")
scores[scores < 100] = 0
print(f"Scores AFTER -> {scores}")
