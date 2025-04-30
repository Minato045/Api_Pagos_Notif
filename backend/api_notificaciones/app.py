from flask import Flask, request, jsonify
from factory_notificacion import NotificacionFactory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/enviar_notificacion", methods=["POST"])
def enviar_notificacion():
    data = request.json
    canal = data["canal"]
    mensaje = data["mensaje"]
    contacto = data.get("contacto")

    contacto = data.get("contacto")

    notificacion = NotificacionFactory.crear_notificacion(canal)

    if canal == "email":
        if not contacto:
            return jsonify({"error": "El campo 'contacto' es obligatorio para el canal 'email'"}), 400
        resultado = notificacion.enviar(contacto, mensaje)  # Pasar el destinatario y el mensaje
    else:
    # Verificar si es SMS y pasar el número de teléfono
        if canal == "sms":
            if not contacto:
                return jsonify({"error": "El número de teléfono es obligatorio para SMS"}), 400
            resultado = notificacion.enviar(contacto, mensaje)  # Pasar el destinatario y el mensaje
        elif canal == "whatsapp":

            if not contacto:
                return jsonify({"error": "El campo 'contacto' es obligatorio para el canal 'whatsapp'"}), 400
            resultado = notificacion.enviar(contacto, mensaje)  # Pasar el destinatario y el mensaje
        else:
            resultado = notificacion.enviar(mensaje)  # Otros canales solo necesitan el mensaje
        
    return jsonify({"resultado": resultado})