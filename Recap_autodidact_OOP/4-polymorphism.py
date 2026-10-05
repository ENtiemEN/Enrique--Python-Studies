''' Módulo 4: Polimorfismo y Duck Typing
-> El término Polimorfismo significa "múltiples formas". En programación, representa la capacidad de tratar diferentes objetos a través de una interfaz común, sin importar su tipo concreto.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
En python, el polimorfismo se apoya de la filosofía de tipado dinámico llamada Duck Typing ("tipado de pato"):

"Si cambina como un pato y grazna como un pato, entonces es un pato"

- En lenguajes como (Java/C++) -> Para que dos clases sean polimórficas, normalmente deben heredar de la misma clase abstracta o implementar la misma interfaz explícita

- En python (Duck typing) -> No importa la jerarquía ni el árbol genealógico del objeto. Lo único relevante es si el objeto posee el método o atributo que se está intentando invocar.
'''

class FacturaPDF:
    def __init__(self, cliente: str, monto: float):
        self.cliente = cliente
        self.monto = monto

    def renderizar(self) -> str:
        return f"[PDF] Generando PDF para {self.cliente} por un total de ${self.monto:.2f}"

class FacturaHTML:
    def __init__(self, cliente: str, monto: float):
        self.cliente = cliente
        self.monto = monto

    def renderizar(self) -> str:
        return f"<html><body><h1>Factura para {self.cliente}</h1><p>Total: ${self.monto}</p></body></html>"

# Esta clase NO tiene ninguna relación de herencia con las anteriores
# PERO COMPARTE EL MÉTODO 'renderizar' (Duck Typing puro)
class NotificacionEmail:
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    def renderizar(self) -> str:
        return f"[EMAIL] Asunto: Resumen de servicio enviado a {self.destinatario}."

# Función polimorfica: no le importa el tipo del objeto, solo que sepa 'renderizar()'
def procesar_documento(renderizable) -> None:
    print(renderizable.renderizar())

# Pruebas
documentos = [
    FacturaPDF("Tech Corp", 1250.00),
    FacturaHTML("Consultora Global", 450.00),
    NotificacionEmail("contacto@empresa.com")
]

for doc in documentos:
    procesar_documento(doc)