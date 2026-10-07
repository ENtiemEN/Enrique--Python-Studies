mynames = ['Enrique','Diana','Mark','Milagros']

# Clasical way de hacer una enumeracion

counter = 0
for name in mynames:
  print(f"({counter}) -> {name}")
  counter += 1


# Usando `enumerate()`

for i,value in enumerate(mynames):
  print(f"({i}) -> {value}")

# Viendo qué hay en `enumerate()` -> me bota un objeto

print(list(enumerate(mynames)))
print(dict(enumerate(mynames)))
