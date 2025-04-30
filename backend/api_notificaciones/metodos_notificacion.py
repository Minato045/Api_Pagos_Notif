# backend/api_notificaciones/metodos_notificacion.py
from interfaces import Notificacion
from dotenv import load_dotenv
from email_conecction import EmailConnection
import os
import pywhatkit 

load_dotenv()
from sms_service import send_sms

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
    def enviar(self, contacto, mensaje):
        """
        Envía un SMS utilizando Textbelt.

        :param contacto: Número de teléfono del destinatario.
        :param mensaje: Mensaje a enviar.
        :return: Resultado del envío.
        """
        estado, resultado = send_sms(contacto, mensaje)
        if estado:
            return f"SMS enviado con ID: {resultado}"
        else:
            return f"Error al enviar SMS: {resultado}"

class Push(Notificacion):
    def enviar(self, mensaje):
        return f"Push Notification enviado con mensaje: {mensaje}"

class WhatsApp(Notificacion):
    def enviar(self, destinatario, mensaje):
        try:
            # Extraer el número sin el prefijo "whatsapp:"
            numero = destinatario.replace("whatsapp:", "")
            # Programar el envío del mensaje para el minuto siguiente
            pywhatkit.sendwhatmsg_instantly(numero, mensaje, wait_time=10)
            return f"WhatsApp enviado a {numero} con mensaje: {mensaje}"
        except Exception as e:
            return f"Error al enviar WhatsApp: {str(e)}"
