# Example 1 -- usando *args
mysum = lambda *args: sum(args)

print(mysum(10,20,30,5))

# Example 2 -- Llamando directamente desde print
print(f"Llamando my lambda expression directamente -> {(lambda x: x ** 3)(5)}")

# Example 3 -- Using `filter()`
numbers = [8, 66, 12, 14, 7, 99, 102, 88, 77]

even_numbers = filter(
  lambda x: x % 2 == 0,
  numbers
)

print(list(even_numbers))

# Example 4 -- Using `map()`

squared_numbers = map(
  lambda x: x ** 2,
  numbers
)
print(list(squared_numbers))

# Retornando una function (Callable function)

def myfunction(num):
  return lambda x: x * num


table_number = int(input('De qué número quieres ver la tabla numérica (1-12): '))

multiplier = myfunction(table_number)

for i in range(1,13):
  print(f"{table_number}x{i}={multiplier(i)}")

