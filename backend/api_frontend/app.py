# backend/api_frontend/app.py
from flask import Flask, request, jsonify
import requests
from factory_tema import get_tema_factory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/realizar_pago_y_notificar", methods=["POST"])
def realizar():
    data = request.json
    tipo_pago = data["tipo_pago"]
    monto = data["monto"]
    canal = data["canal"]
    tema = data["tema"]

    # Procesar pago
    pago_res = requests.post("http://localhost:5001/procesar_pago", json={"tipo": tipo_pago, "monto": monto}).json()

    # Notificar
    notificacion_res = requests.post("http://localhost:5002/enviar_notificacion", json={"canal": canal, "mensaje": pago_res["resultado"]}).json()

    # HTML dinámico con el tema
    factory = get_tema_factory(tema)
    html = f"""
        <html>
            {factory.crear_header()}
            <body>
                <h2>Resultado:</h2>
                <p>{notificacion_res["resultado"]}</p>
            </body>
            {factory.crear_footer()}
        </html>
    """
    return html
