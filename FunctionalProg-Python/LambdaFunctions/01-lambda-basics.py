'''
Syntax
  lambda parameters: expression

A lambda expression creates an anonymous function object.

It may contain:
- zero or more parameters
- exactly one expression

The expression is evaluated when the function is called, not when the lambda is created.

The result of the expression becomes the return value automatically


lambda expression
      ↓ (evaluates to)
function object
      ↓ (can be called)
    result
'''

# ============= BASICS ==============
square = lambda x: x ** 2
# `lambda _: ...` -> is an expression whose resulting value is a function object
print(square(5))
print(type(square)) #-> <class 'function'>

constant = lambda: '16|11|13'
#print(constant) #-> <function <lambda> at 0x7e1a26201440>
print(constant())

# ============ LAMBDA vs DEF ============
'''
  def
- statement
- creates a named function
- supports multiple statements
- annotations
- docstrings
- easier debugging

  lambda
- expression
- usually anonymous
- exactly one expression
- intended for short functions
'''

# ==== Lambda with multiple parameters ====
add = lambda x,y: x+y
print(add(3,7))

# ==== Lambda with NO parameters ====
get_pi = lambda: 3.14159265368979
print(get_pi)

# A lambda is a first-class function object
f = lambda x: x+1

g = f

print(f(10)) # 11
print(g(10)) # 11
# `f` and `g` refer to the same function object

print(f is g) #True


# ==== Lambda expression itself can be called immediately  ====

result = (lambda x: x * 2)(5)
print(result) # 10
# lambda _:... -> creates a function object -> function is called with an argument -> result

# ==== Lambdas may use expressions ====

absolute_value = lambda x: x if x >= 0 else -x

print(absolute_value(-10))

# ==== Lambdas cannot contain arbitrary statements ====

'''
Invalid idea

lambda x:
  y = x*2
  return y

A lambda body must be a single expression.

Assigment statements, loops, `return`, etc. Cannot normaly appear as the lambda body
'''

# ==== Functions are values ====

operations = [
  lambda x: x+1,
  lambda x: x*2,
  lambda x: x**2,
]

value = 3

for operation in operations:
  print(operation(value))

# The list stores function objects just like it could store integers, strings, tuples, etc.

