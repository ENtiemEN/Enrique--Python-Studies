''' Modulo 5: Abstracción con el Módulo `abc`
-> La abstracción oculta los detalles complejos de implementación y expone únicamente una interfaz obligatoria.
Mientras que el 'Duck Typing' confía en que el programador implemente los métodos correctos, las *Clases Base Abstractas(ABC)* fuerzan contractualmente a las subclases a implementar ciertos métodos antes de permitir su instanciación

--- --- --- --- --- --- --- --- --- --- --- --- --- --- 

Pyton incluye el módulo estándar `abc` (Abstract Base Classes):

- `ABC` -> Clase base de la que se hereda para convertir una clase en abstracta. No se puede instanciar directamente

- `@abstractmethod` -> Decorador que marca métodos como obligatorios. Si una subclase no define este método Python lanzará un `TypeError` inmediatamente al intentar crear el objeto
'''

from abc import ABC, abstractmethod

class PasarelaPago(ABC):
    """Clase base abstracta: define el contrato obligatorio para cualquier pasarela."""

    def __init__(self, moneda: str = "USD"):
        self.moneda = moneda

    @abstractmethod
    def autenticar(self) -> bool:
        """Debe validar las credenciales de la pasarela"""
        pass

    @abstractmethod
    def procesar_cobro(self, monto: float) -> bool:
        """Debe ejecutar el cobro según la API del proveedor"""
        pass

    # Un método concreto dentro de una clase abstracta
    def registrar_log(self, mensaje: str) -> None:
        print(f"[AUDITORIA - {self.moneda}]: {mensaje}")

# obs: Stripe es una plataforma de servicios financieros y procesamiento de pagos en línea
class PagoStripe(PasarelaPago):
    def __init__(self, api_key: str, moneda: str = "USD"):
        super().__init__(moneda)
        self.api_key = api_key

    def autenticar(self) -> bool:
        return self.api_key.startswith('sk_live_')

    def procesar_cobro(self, monto: float) -> bool:
        if self.autenticar():
            self.registrar_log(f"Cobro exitoso de ${monto:.2f} vía Stripe API.")
            return True
        print("Error: API Key de Stripe inválida")
        return False

class PagoIncompleto(PasarelaPago):
    """Subclase errónea: olvida implementar 'procesar_cobro'."""
    def autenticar(self) -> bool:
        pass

    # ¿Falta definir el método `procesar_cobro()`?
    # def procesar_cobro(self, monto: float) -> bool:
    #     pass

    def mensaje_aviso(self) -> None:
        print("Se completaron los métodos abstractos de la clase incompleta'")

# Bloque de prueba ---
stripe = PagoStripe("sk_live_314159265358979323")
print(f"¿API procesada correctamente? -> {stripe.autenticar()}")

stripe.procesar_cobro(580.00)

# 3. Intento de instanciar subclase con contrato incompleto
try:
    incompleto = PagoIncompleto()
    incompleto.mensaje_aviso()
except TypeError as e:
    print(f"Bloqueo 2 (Falta método abstracto): {e}")