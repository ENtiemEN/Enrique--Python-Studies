''' Modulo 6: Atributos Gestionados con `@property`
-> En lenguajes como Java o C++, es común escribir métodos explícitos como `get_precio()` y `set_precio(valor)`. En python esto se considera anti-patrón (no pythonic)

-> Python resuelve esto con el decorador `@property`, que implementa el 'protocolo descriptor': permite acceder a un método con la sintaxis limpia de un atributo común (`objeto.precio`), pero ejecutando lógica por detrás (validaciones, cálculos en tiempo real o control de acceso)

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

- Getter (`@property`) --> Se ejecuta al leer el valor (`print(p.precio)`)

- Setter (`@<nombre>.setter`) --> Se ejecuta al asignar un valor (p.precio = 50). Ideal para validaciones de negocio

- Deleter (`@<nombre>.deleter`) --> Se ejecuta al usar la palabra reservada `del` (`del p.precio`). Útil para reiniciar estados o liberar recursos
'''

class Producto:
    def __init__(self, nombre: str, precio_unitario: float):
        self.nombre = nombre
        self.precio_unitario = precio_unitario

    # 1. GETTER
    @property
    def precio_unitario(self) -> float:
        """Dvuelve el precio almacenado de forma privada."""
        return self._precio_unitario

    # 2. SETTER
    @precio_unitario.setter
    def precio_unitario(self, nuevo_precio: float) -> None:
        """Valida que el precio no sea negativo ni cero"""
        if not isinstance(nuevo_precio, (int,float)):
            raise TypeError("El precio debe ser un número entero o flotante.")
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser estrictamente mayor a 0.")

        self._precio_unitario = float(nuevo_precio)

    # ----------------------------

    # 3. PROPIEDAD DE SOLO LECTURA (aprox)
    @property
    def precio_con_iva(self) -> float:
        """Calcula el 18% de IVA en tiempo real sin almacenarlo"""
        return round(self._precio_unitario * 1.18, 2)

    # 4. DELETER
    @precio_unitario.deleter
    def precio_unitario(self) -> None:
        """Permite borrar o resetear el atributo."""
        print(f"[LOG] Reseteando el precio de '{self.nombre}' a 0.0")
        self._precio_unitario = 0.0


teclado = Producto("Teclado Mecánico", 80.0)

# Acceso natural como atributo (invoca el getter)
print(f"Producto: {teclado.nombre}")
print(f"Precio base: ${teclado.precio_unitario}")
print(f"Precio con IVA: ${teclado.precio_con_iva}")

# Modificación válida
teclado.precio_unitario = 76.50
print(f"El nuevo valor del producto (Sin IVA) es: ${teclado.precio_unitario}")

# Intentos de modificación inválida (Validación del Setter)
try:
    teclado.precio_unitario = -4.58
except ValueError as e:
    print(f"\nError capturado en Setter: {e}")

try:
    teclado.precio_unitario = "Precio"
except TypeError as e:
    print(f"\nError capturado en Setter: {e}")

# Intento de escritura en una propiedad DE SOLO LECTURA
try:
    teclado.precio_con_iva = 100.00     # Lanza AttributeError (no tiene .setter)
except AttributeError as e:
    print(f"Error capturado (solo lectura)")


print("=== === === === === === === === === === === ===")
# Borrado del atributo (invoca al deleter, mediante `del`)
del teclado.precio_unitario
print(f"Precio tras borrado: ${teclado.precio_unitario}")