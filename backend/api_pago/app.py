from flask import Flask, request, jsonify
from factory_pago import PagoFactory
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # <-- Y esto también

@app.route("/procesar_pago", methods=["POST"])
def procesar_pago():
    data = request.json
    tipo = data["tipo"]
    monto = data["monto"]
    pago = PagoFactory.crear_pago(tipo)
    resultado = pago.procesar_pago(monto)
    return jsonify({"resultado": resultado})