'''
    (Favor Composition over Inheritance) -- Composición sobre Herencia
    La herencia expresa una relación de tipo "es un" (is-a), mientras que la composición expresa una relación de tipo "tiene un" (has-a)

    Problema:
    Imagina modelar un sistema de notificaciones. Si heredas:
    - ´NotificacionEmail´
    - ´NotificacionSMS´
    - ´NotificacionEmailYSMS´ (Empieza la duplicación o explosión de subclases si agregas Slack, WhatsApp, etc.)

    Solución --> Refactorización a Composición
    Separamos la estrategia de envío del servicio de alertas. El servicio recibe (tiene) uno o varios canales de envio
'''

from abc import ABC, abstractmethod

# 1. Componente aislados
class CanalNotificacion(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, mensaje: str) -> None:
        pass

class EnvioEmail(CanalNotificacion):
    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"[Email -> {destinatario}] {mensaje}")

class EnvioSMS(CanalNotificacion):
    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"[SMS -> {destinatario}] {mensaje}")

class EnvioSlack(CanalNotificacion):
    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"[Slack Channel -> {destinatario}] {mensaje}")

# 2. Clase Contenedora: Compone los canales (Inyección de dependencias)
class GestorAlertas:
    def __init__(self, canales: list[CanalNotificacion] = None):
        self.canales = canales if canales is not None else []

    def registrar_canal(self, canal: CanalNotificacion) -> None:
        self.canales.append(canal)

    def alertar(self, destino: str, mensaje: str) -> None:
        print(f"\n --- Disparando Alerta : {mensaje} ---")
        for canal in self.canales:
            canal.enviar(destino, mensaje)


# PRUEBA

# Configuración 1: Sistema que solo envía Emails
email_service = EnvioEmail()
alerta_usuario = GestorAlertas([email_service])
alerta_usuario.alertar("enrique@empresa.com", "Bienvenio a la plataforma")

# Configuracion 2: Sistema critico que envía por Email, SMS y Slack en simultáneo
# Sin necesidad de crear subclases
alerta_critica = GestorAlertas([
    EnvioEmail(),
    EnvioSMS(),
    EnvioSlack()
])

alerta_critica.alertar("admin-ops", "Error 500")