# backend/api_notificaciones/metodos_notificacion.py
from interfaces import Notificacion

class Email(Notificacion):
    def enviar(self, mensaje):
        return f"Correo enviado con mensaje: {mensaje}"

class SMS(Notificacion):
    def enviar(self, mensaje):
        return f"SMS enviado con mensaje: {mensaje}"

class Push(Notificacion):
    def enviar(self, mensaje):
        return f"Push Notification enviado con mensaje: {mensaje}"

class WhatsApp(Notificacion):
    def enviar(self, mensaje):
        return f"WhatsApp enviado con mensaje: {mensaje}"
