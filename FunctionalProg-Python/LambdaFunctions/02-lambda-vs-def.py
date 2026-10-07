'''
Both 'lambda' and 'def' create function objects, buy they are not equivalent.

Main distinction:
  `def`    -> statement
  `lambda` -> expression

This matters because expressions can appear inside other expressions, while statements cannot.

General forms:

  def function_name(parameters):
    statement
    return value

  lambda parameters: expression
'''

# ==== 1. Both create function objects ====
def square_def(x):
  return x**2

square_lambda = lambda x: x**2

print(type(square_def))
print(type(square_lambda))
