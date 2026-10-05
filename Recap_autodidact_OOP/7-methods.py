''' Módulo 7: Tipos de Métodos (`self`, `@classmethod` y `@staticmethod`)
-> Python clasifica los métodos según el nivel de contexto al que tienen acceso:

    Tipo      |    Decorador    | Primer argumento 

a)  Instancia |  (ninguno)      |   self

b)  Clase     |  @classmethod   |   cls

c)  Estático  |  @staticmethod  |   (ninguno implícito)


    Acceso a estado                 |       Caso de uso

a]  Accede y modifica el estado         Métodos normales de
    del objeto y de la clase            lógica de negocio

b]  Accede y modifica el estado     |   Constructores
    de la clase (no va `self`)          alternativos (factories)

c]  Aislado: no accede ni a         |   Funciones utilitarias
    `self` ni a `cls`                   asociadas lógicamente
                                        a la clase
'''

import json

class Usuario:
    # Atributo de clase compartido
    dominio_predeterminado = "empresa.com"

    def __init__(self, alias: str, rol: str = "estándar"):
        self.alias = alias
        self.rol = rol

    # 1. MÉTODO DE INSTANCIA: conoce a 'self'
    def obtener_email_corporativo(self) -> str:
        return f"{self.alias}@{Usuario.dominio_predeterminado}"

    # 2. MÉTODO DE CLASE: conoce a 'cls', no al objeto individual
    # "Muy usado como constructor alternativo para parsear diferentes formatos"
    @classmethod
    def desde_string(cls, formato_texto: str) -> "Usuario":
        """
            Crea una instancia a partir de cada cadena tipo 'alias:rol'
        """
        alias, rol = formato_texto.split(':')
        return cls(alias.strip(), rol.strip()) # <-- Creando una isntancia de la clase i.e. Usuario(_, _)

    # `cls` representa la clase sobre la que estás invocando el método clase
    @classmethod
    def desde_json(cls, datos_json: str) -> "Usuario":
        """
            Crea una instancia parseando un payload JSON.
        """
        datos = json.loads(datos_json)

        # if "rol" in datos:
        #     return cls(alias=datos["alias"], rol=datos["rol"])
        # else:
        #     return cls(alias=datos["alias"])
        
        return cls(alias=datos["alias"], rol=datos.get("rol", "estándar"))

    # 3. MÉTODO ESTÁTICO: no recibe ni 'self', ni 'cls'
    @staticmethod
    def validar_alias(alias: str) -> bool:
        """Comprueba reglas de alias sin necesitar instanciar la clase."""
        return alias.isalnum() and len(alias) >= 3

# Prueba
# 1. Uso del método estático sin instanciar
## .isalnum() -> A-Z a-z 0-9 <> (True)
print("Validación 'us1': ", Usuario.validar_alias('us1'))
print("Validación 'a': ", Usuario.validar_alias('a'))

# 2. Instanciación estándar
u1 = Usuario("carlos", "admin")
print("\nInstancia directa: ", u1.obtener_email_corporativo())

# 3. Constructores alternativos con @classmethod
u2 = Usuario.desde_string("valeria:soporte")
print(f"Desde una string: Alias -> {u2.alias} | Rol -> {u2.rol}")
print(f"Desde una string: {u2.obtener_email_corporativo()}")

print("=== === === === === === === === ===")

u3 = Usuario.desde_json('{"alias": "mateo", "rol": "auditor"}')
u4 = Usuario.desde_json('{"alias": "Enrique"}')

print(f"Desde JSON: Alias -> {u3.alias} | Rol -> {u3.rol}")
print(f"Desde JSON: {u3.obtener_email_corporativo()}")

print(f"\nDesde JSON: Alias -> {u4.alias} | Rol -> {u4.rol}")
print(f"Desde JSON: {u4.obtener_email_corporativo()}")
