''' Módulo 8: Métodos Especiales (Dunder Methods) y Sobrecarga de Operadores

-> Los métodos con doble guion bajo ('double underscore o *dunder*') permiten integrar tus clases directamente con la sintaxis nativa de Python.
En lugar de inventar métodos como `sumar()`, `imprimir()` o `longitud()`, implementas los dunder corespondientes y Python los llama automáticamente cuando usas operadores o funciones integradas:

- `__str__` --> Representación legible e informal pensada para el usuario final (`print(obj)` o `str(obj)`)

- `__repr__` --> Representación inequívoca y formal orientada al desarrollador o depuración (`repr(obj)` o en la consola interactiva). Lo ideal es que parezca el código exacto necesario para recrear el objeto

- `__len__` --> Define el comportamiento al pasar el objeto a la función `len(obj)`. Debe retornar un entero no negativo

- Sobrecarga de operadores (`__add__`, `__eq__`, etc.) --> Permite que tus objetos interactúen con operadores como `+`, `==`, `<`, etc.
'''

class CarritoCompras:
    def __init__(self, cliente: str):
        self.cliente = cliente
        # type(tuple([str, float])) -> <class 'tuple'>
        # type(tuple[str, float]) -> <class 'types.GenericAlias'>
        self.items: list[tuple[str, float]] = []
        # [(str, float), (str, float), ..., (str, float)]

    def agregar(self, item: str, precio: float) -> None:
        self.items.append((item, precio))

    # 1. Función len():
    def __len__(self) -> int:
        return len(self.items)

    # 2. Representación para depuración: repr(carrito)
    def __repr__(self) -> str:
        return f"CarritoCompras(cliente='{self.cliente}')"

    # 3. Representación legible: print(carrito)
    def __str__(self) -> str:
        total = sum(precio for _, precio in self.items)
        return f"Carrito de {self.cliente} ({len(self)} artículos) - Total: ${total}"

    # 4. Sobrecarga de suma (+): carrito1 + carrito2
    def __add__(self, otro: "CarritoCompras") -> "CarritoCompras":
        """Fusiona dos Carritos en uno nuevo combinando sus artículos"""
        if not isinstance(otro, CarritoCompras):
            return NotImplemented

        nuevo_carrito = CarritoCompras(f"{self.cliente} & {otro.cliente}")

        nuevo_carrito.items = self.items + otro.items
        return nuevo_carrito

    # Sobrecarga de igualdad (==): carrito1 = carrito2
    def __eq__(self, otro: object) -> bool:
        """Determina que dos carritos son iguales si tienen el mismo valor total"""
        if not isinstance(otro, CarritoCompras):
            return NotImplemented
        total_self = sum(precio for _ ,precio in self.items)
        total_otro = sum(precio for _,precio in otro.items)
        return total_self == total_otro

# Testeo
c1 = CarritoCompras("Enrique")
c1.agregar("Teclado", 108.0)
c1.agregar("Mouse", 100.0)

c2 = CarritoCompras("Diana")
c2.agregar("Monitor", 306.00)

# __str__ y __repr__
print(str(c1))
print(str(c2))
#print(repr(c1))

# Uso del __len__
print(f"Total de artículos en c1: {len(c1)}")

# Sobrecarga de igualdad -> __eq__
print(f"¿Valen lo mismo c1 y c2? -> {c1 == c2}")

# Sobrecarga de suma -> __add__
c_combinado = c1 + c2
print(str(c_combinado))
print(f"Artículos fusionados: {len(c_combinado)}")