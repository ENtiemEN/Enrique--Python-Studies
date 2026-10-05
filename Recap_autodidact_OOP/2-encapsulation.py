''' ENCAPSULACIÓN Y PROTECCIÓN DE DATOS
-> El encapsulamiento restringe el acceso directo al estado interno de un objeto para evitar modificaciones accidentales (o intencionales) o inválidas.

A diferencia de Java, C++. Python no tiene "palabras reservadas" como `private` o `protected` a nivel de compilador.
En su lugar utiliza convenciones y una técnica llamada *Name Mangling* (Ofuscación de nombres)

- Público (`atributo`) -> Accesible desde cualquier lugar

- Protegido (`_atributo`) -> Convención comunitaria (_ guion abajo). i.e. "No tocar esto fuera de las clases o subclases". No hay bloqueo sintáctico

- Privado (`__atributo`) -> Dos guiones bajos activan el *name mangling*. Python renombra internamente la variable a `_NombreClase__atributo` para prevenir colisiones en herencia y accesos directos descuidados
'''

class BilleteraDigital:
    def __init__(self, usuario: str, saldo_inicial: float, pin: str):
        self.usuario = usuario  # Público
        self._limite_diario = 1000.00   # Protegido (conveción)
        self.__pin = pin    # privado (name mangling)
        self.__saldo = saldo_inicial    # privado (name mangling)

    def transferir(self, monto: float, pin_ingresado: str) -> bool:
        """Método público que controla la lógica de negocio y protege datos"""
        if pin_ingresado != self.__pin:
            print("Error: PIN incorrecto")
            return False

        if monto > self._limite_diario:
            print(f"Error: Excede el límite diario de ${self._limite_diario}")
            return False

        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Transferencia de ${monto:.2f} realizada con éxito.")
            return True
        else:
            print("Error: Fondos insuficientes o monto inválido")
            return False

    def consultar_saldo(self, pin_ingresado: str) -> None:
        if pin_ingresado == self.__pin:
            print(f"Saldo disponible de {self.usuario}: ${self.__saldo:.2f}")
        else:
            print("Error: Autenticación fallida al consultar saldo.")

# instanciamos una billetera
billetera = BilleteraDigital("Valeria", 500.00, "1234")

# 1. USO CORRECTO vía interfaz pública
billetera.transferir(120.0, "1234")
billetera.consultar_saldo("1234")

# 2. Intento de acceso directo a un atributo privado
try:
    print(billetera.__saldo)    # Lanza AttributeError
except AttributeError as e:
    print(f"\nBloqueo esperado: {e}")

# 3. Inspección del 'Name Mangling'
# Python no lo destruyó, solo lo renombró a: _BilleteraDigital__saldo
print(f"Acceso forzado vía mangling: ${billetera._BilleteraDigital__saldo:.2f}")