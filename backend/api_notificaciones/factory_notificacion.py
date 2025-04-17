from metodos_notificacion import Email, SMS, Push, WhatsApp

class NotificacionFactory:
    @staticmethod
    def crear_notificacion(canal):
        if canal == "email":
            return Email()
        elif canal == "sms":
            return SMS()
        elif canal == "push":
            return Push()
        elif canal == "whatsapp":
            return WhatsApp()
        else:
            raise ValueError("Canal no soportado")