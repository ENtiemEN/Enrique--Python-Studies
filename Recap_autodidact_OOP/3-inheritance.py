''' Herencia y delegación con `super()`
-> La herencia permite que una clase secundaria (hija) reutilice, extienda o modifique los atributos y comportamientos de una clase principal (padre).

- `super()` -> Función que devuelve el objeto proxy que delega las llamadas de métodos a una clase base. Se usa comúnmente en el `__init__` de la subclase para garantizar que los atributos del padre se inicialicen correctamente sin acoplar el código al nombre explícito de la clase base

- "Overriding" (Sobreescritura de métodos) -> La clase hija redefine un método de la clase padre para adaptar su comportamiento
'''

''' Errores comunes
- Olvidar llamar a `super().__init__(...)` -> Provoca que los atributos de la clase padre nunca se creen en la instanacia hija lanzando `AtributteError` en tiempo de ejecución.

- Sobreescribir y duplicar la lógica en vez de extender -> Reescribir todo el método del padre en la hija en lugar de llamar al método base con `super().metodo()` y solo agregar lo nuevo
'''

class Empleado:
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self) -> float:
        return self.salario_base

    def describir(self) -> str:
        return f"Nombre: {self.nombre} | Salario: ${self.calcular_pago():.2f}"

class Desarrollador(Empleado):
    def __init__(self, nombre: str, salario_base: float, lenguaje: str):
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje

    def describir(self) -> str:
        base_info = super().describir()
        return f"{base_info} | Lenguaje principal: {self.lenguaje}"

class Gerente(Empleado):
    def __init__(self, nombre: str, salario_base: float, bono_anual: float = 0.8):
        super().__init__(nombre, salario_base)
        self.bono_anual = bono_anual

    def calcular_pago(self) -> float:
        # Sobreescritura completa del método de cálculo
        return self.salario_base + self.bono_anual

# Instanciando
dev = Desarrollador("Sofía", 3200.00, "Python")
gerente = Gerente("Mateo", 5000.0, bono_anual=1200.0)

print(dev.describir())
print(dev.calcular_pago())

print("==========================")

print(gerente.describir())
print(gerente.calcular_pago())

# Verificando la relación de tipos
print(f"\n¿'dev' es una instancia de Desarrollador?: {isinstance(dev, Desarrollador)}")
print(f"¿'dev' es una instancia de Empleado?: {isinstance(dev, Empleado)}")

print(f"\n¿Es Desarrolador una subclase de Empleado?: {issubclass(Desarrollador, Empleado)}")