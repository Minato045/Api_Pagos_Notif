import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailConnection:
    def __init__(self, smtp_server, port, email, password):
        self.smtp_server = smtp_server
        self.port = port
        self.email = email
        self.password = password

    def enviar_correo(self, destinatario, asunto, mensaje):
        try:
            # Crear el mensaje
            msg = MIMEMultipart()
            msg["From"] = self.email
            msg["To"] = destinatario
            msg["Subject"] = asunto
            msg.attach(MIMEText(mensaje, "plain"))

            # Conectar al servidor SMTP
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.sendmail(self.email, destinatario, msg.as_string())
            return "Correo enviado exitosamente"
        except smtplib.SMTPException as e:
            return f"Error SMTP: {str(e)}"
        except Exception as e:
            return f"Error general: {str(e)}"