'''
    __repr__ (Representación) -> Diseñado para desarrolladores, depuración (debugging) y logs. Su objetivo es ser inequívoco (unambiguous). Si es posible, debe parecer código Python válido para recrear el objeto.

    __str__ (String) -> Diseñado para el usuario final. Su objetivo es ser legible (readable), estético y fácil de interpretar en interfaces de usuario o salidas de texto comunes

    ```python
    # Ejemplo de la librería estandar `datetime`
    import datetime

    hoy = datetime.date(2026,9,20)
    print(str(hoy)) # '2026-09-20'

    print(repr(hoy)) # 'datetime.date(2026, 9, 20)'
    ```
'''
# Dunder -> __
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructed!")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Vector) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __mul__(self, other: Vector):
        return self.x * other.x + self.y * other.y

    def __len__(self) -> int:
        return 2
    
    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return f"Vector({self.x},{self.y})"

    def __call__(self):
        print("HII! I was called!")

    
p = Person("Mike", 25)
print(p.name)
print(p.age)
'''
`del p` no destruye directamente el objeto. Formalmente elimina el nombre `p` del namespace local.
p --> Person object
después de `del p`
La referencia `p` desaparece.
p     Person object
Si no existe niguna referencia al objeto, entonces el objeto queda elegible para ser recolectado. (Reference Counting | Garbage Collector)
'''
del p

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = Vector(60, 80)
try:
    v3 = v1 + v2
    print(v3)    
    print(len(v3))
    print(f"The vectors are equal ({v3 == (v1+v2)})")
    print(f"{v1} * {v2} = {v1 * v2}")
except TypeError as e:
    print(f"Error -> {e}")

v3()

vectors = [Vector(1,2), Vector(3,4), Vector(5,6)]
print(vectors)