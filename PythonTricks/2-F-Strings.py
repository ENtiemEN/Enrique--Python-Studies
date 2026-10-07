name = "Mike"
age = 25
promedio = 16.467
num_fav = 3.14159265358979323

print("Mi nombre es " + name + " tengo " + str(age) + " años")

print("Nombre: %s, Edad: %d, Num. Fav: %.2f" % (name,age,num_fav))

print("Nombre: {}, Edad: {}, Num. Fav: {:.2f}".format(name,age,num_fav))

print(f"Nombre: {name}, Edad: {age}, Num. Fav: {num_fav:.2f}")
