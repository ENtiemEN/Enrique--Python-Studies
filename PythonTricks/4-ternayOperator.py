age = 12 # user input
#adult = age >= 18
#print(adult)

# Procedural Approach

def revisarMayoriaEdad(flag) -> None:
  if flag:
    print("Es adulto")
  else:
    print("No es adulto")

# Procedural Approach
if age >= 18:
  adult = True
else:
  adult = False

revisarMayoriaEdad(adult)

# Usin Ternary Operator

adult = True if age >= 18 else False

print("Eres adulto" if adult else "No eres un adulto")

# Multiple Ternary Operators

number = 100

print("Numero muy muy grande" if number>1000 else "Numero grande" if number>100 else "Numero pequeño pero aún positivo" if number>0 else "Numero negativo")


