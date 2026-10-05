# ===============================================================================================================
''' Guía
1. Clases, objetos, constructor (`__init__`) y rol del `self`
2. Cuatro pilares: Encapsulamiento, Abstracción, Herencia, Polimorfismo y Abstracción
3. Tipos de métodos (`@classmethod`, `@staticmethod`) y propiedades (`@property`)
4. Métodos especiales /dunder methods (`__str__`, `__repr__`, sobrecarga de operadores), composición y `dataclasses`
'''

# ===============================================================================================================

''' Una CLASE es el plano de construcción; un objeto o instancia es lo construido a partir de ese plano.

- `self` --> representa la instancia concreta que ejecuta el código, permitiendo aislar sus datos de otras instancias.

- `__init__` --> es el método inicializador que se ejecuta automáticamente al instanciar
'''

# Diferencia entre argumento y parámetro: un argumento es el valor que se pasa a una función, mientras que un parámetro es la variable que recibe ese valor dentro de la función.

class CuentaBancaria:
    # Atributo de clase: compartido por todas las instancias
    banco = "Banco Central"

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        # Atributos de instancia: únicos para cada objeto
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto: float) -> None:
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto:.2f} exitoso en la cuenta de {self.titular}")
        else:
            print("El monto a depositar debe ser positivo.")

    def mostrar_estado(self) -> None:
        print(f"Titular: {self.titular} | Saldo: {self.saldo:.2f} | Banco: {self.banco}")

# instanciamos un objeto de la clase CuentaBancaria
cuenta_ana = CuentaBancaria("Ana", 150.0)
cuenta_carlos = CuentaBancaria("Carlos")

cuenta_ana.depositar(100.0)
cuenta_ana.mostrar_estado()