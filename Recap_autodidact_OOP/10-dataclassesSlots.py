''' ´dataclases´ y Optimización con __slots__
    En python existen dos herramientas para estructurar datos eficientemente sin escribir código repetitivo (boilerplate):
    
    1. @dataclass (Módulo ´dataclasses´) -> Genera automáticamente métodos dunder comunes (´__init__´, ´__repr__´, ´__eq__´, etc) a partir de anotaciones de tipo.

    2. ´__slots__´ -> Por defecto, los objetos en Python guardan sus atributos en un diccionario dinámico (´__dict__´). Esto da flexibilidad (puedes agregar atributos sobre la marcha), pero consume mucha memoria RAM por cada instancia.
    ´__slots__´ elimina ´__dict__´ y reserva memoria en un arreglo estático de tamaño fijo
'''

import sys
from dataclasses import dataclass, field

# Clase TRADICIONAL (Con diccionario dinámico)
class RegistroEstandar:
    def __init__(self, id_evento: int, etiqueta: str, valor: float):
        self.id_evento = id_evento
        self.etiqueta = etiqueta
        self.valor = valor

# DATACLASS moderna OPTIMIZADA con Slots
@dataclass(slots=True, forzen=True)
class MetricaOptimizada:
    id_evento: int
    etiqueta: str
    valor: float
    # Atributo con valor por defecto generado por una función
    tags: tuple[str, ...] = field(default_factory=tuple)

# Prueba

obj_estandar = RegistroEstandar(101, "cpu_load", 78.5)
obj_optimizado = MetricaOptimizada(101, "cpu_load", 78.5, tags=("servidor-1", "produccion"))

# A. __repr__ automático y legible
print("Dataclass repr:", obj_optimizado)

# B. Comparación por valor automática (__eq__)
otro_optimizado = MetricaOptimizada(101, "cpu_load", 78.5, tags=("servidor-1", "produccion"))

print("¿Son idénticos en datos?: ", obj_optimizado == otro_optimizado)

# C.