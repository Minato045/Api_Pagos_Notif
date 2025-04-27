# backend/api_notificaciones/metodos_notificacion.py
from interfaces import Notificacion
from dotenv import load_dotenv
from email_conecction import EmailConnection
import os

load_dotenv()

class Email(Notificacion):
    def __init__(self):
        # Configuración de Gmail usando variables de entorno
        self.email_connection = EmailConnection(
            smtp_server="smtp.gmail.com",
            port=587,
            email=os.getenv("EMAIL_USER"),  # Cargar correo desde .env
            password=os.getenv("EMAIL_PASSWORD")  # Cargar contraseña desde .env
        )

    def enviar(self, destinatario, mensaje):
        asunto = "Notificación de Pago Realizado EXITOSAMENTE"
        resultado = self.email_connection.enviar_correo(destinatario, asunto, mensaje)
        return resultado
    
class SMS(Notificacion):
    def enviar(self, mensaje):
        return f"SMS enviado con mensaje: {mensaje}"

class Push(Notificacion):
    def enviar(self, mensaje):
        return f"Push Notification enviado con mensaje: {mensaje}"

class WhatsApp(Notificacion):
    def enviar(self, mensaje):
        return f"WhatsApp enviado con mensaje: {mensaje}"
