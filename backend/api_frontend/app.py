# backend/api_frontend/app.py
from flask import Flask, request, jsonify
import requests
from factory_tema import get_tema_factory
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})



@app.route("/realizar_pago_y_notificar", methods=["POST"])
def realizar():
    data = request.json
    tipo_pago = data["tipo_pago"]
    monto = data["monto"]
    canal = data["canal"]
    tema = data["tema"]
    contacto = data.get('contacto') 

    # Procesar pago
    pago_res = requests.post("http://localhost:5001/procesar_pago", json={
        "tipo": tipo_pago,
        "monto": monto
    })
    if pago_res.status_code != 200:
        return jsonify({"error": "Error al procesar el pago"}), 500
    pago_res = pago_res.json()

    # Notificar
    notificacion_res = requests.post("http://localhost:5002/enviar_notificacion", json={
        "canal": canal,
        "mensaje": pago_res["resultado"],
        "contacto": contacto
    })
    if notificacion_res.status_code != 200:
        return jsonify({"error": "Error al enviar la notificación"}), 500
    notificacion_res = notificacion_res.json()

    # Generar reporte PDF
    pdf_report_res = requests.post("http://localhost:5006/generar_reporte_pago", json={
        "tipo": tipo_pago,
        "monto": monto,
        "includeLogo": True,
        "title": "Reporte de Pago",
        "includePaymentDetails": True,
        "includeUserInfo": False,
        "theme": "LIGHT" if tema == "claro" else "DARK",
        "includeTimestamp": True,
        "footerMessage": "Gracias por su pago",
        "format": "A4"
    })
    if pdf_report_res.status_code != 200:
        return jsonify({"error": "Error al generar el reporte PDF"}), 500

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
