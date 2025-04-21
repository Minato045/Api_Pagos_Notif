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
    notificacion = NotificacionFactory.crear_notificacion(canal)
    resultado = notificacion.enviar(mensaje)
    return jsonify({"resultado": resultado})