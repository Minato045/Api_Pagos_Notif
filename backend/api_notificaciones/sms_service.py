import requests

# Clave de API de Textbelt
TEXTBELT_API_KEY = "textbelt"  # Cambia esto por tu clave de API si tienes una clave premium

def send_sms(contacto, message):
    """
    Envía un SMS utilizando la API de Textbelt.

    :param contacto: Número de teléfono del destinatario (en formato internacional, ej. +573178884484).
    :param message: Mensaje a enviar.
    :return: Una tupla con el estado (True/False) y el resultado o el error.
    """
    try:
        # Llamada a la API de Textbelt
        response = requests.post("https://textbelt.com/text", {
            "phone": contacto,
            "message": message,
            "key": TEXTBELT_API_KEY
        })

        # Procesar la respuesta
        result = response.json()
        if result.get("success"):
            return True, result.get("textId")  # Devuelve el ID del mensaje si se envió correctamente
        else:
            return False, result.get("error")  # Devuelve el error si falló
    except Exception as e:
        print(f"Error al enviar SMS: {e}")
        return False, str(e)
