numbers = [10, 11, 40, 50, 47, 79]

even = lambda x: x % 2 == 0

# Solo podemos pasarle una collection de boolean values a las funciones `any()`, `all()`
# Tenemos que construir esas funciones usando -> List comprenhension

result_even = [even(n) for n in numbers]

if any(result_even):
  print("Al menos un número es par")
else:
  print("No hay números pares")

if all(result_even):
  print("Todos los números son pares")
