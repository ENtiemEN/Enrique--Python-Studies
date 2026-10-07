numbers = [14,23,8,12,2,5,90]

# Procedural way
def square(x):
  return x * x

new_list = []
for i in numbers:
  new_list.append(square(i))

print(new_list)

# List Comprenhension
square_list = [square(number) for number in numbers]
print(square_list)

# Map function
''' Obs
En versiones anteriores de Python, cuando no habían List comprenhensions, la funcion `map()` sí fue importante porque hacía leer el código más limpio (Ahora se podría decir que con LC se ve más limpio el código)
'''

map_list = map(square, numbers)
print(list(map_list))
