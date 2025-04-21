from ReportBuilder import ReportBuilder
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)

@app.route("/generar_reporte_pago", methods=["POST"])
def generar_reporte_pago():
    try:
        # Validar datos de entrada
        data = request.json
        if not data:
            return jsonify({"error": "No se proporcionaron datos en la solicitud"}), 400

        tipo = data.get("tipo")
        monto = data.get("monto")
        if not tipo or not monto:
            return jsonify({"error": "Faltan datos obligatorios: 'tipo' o 'monto'"}), 400

        resultado = data.get("resultado", "Pago exitoso")  # Valor por defecto si no se proporciona
        include_logo = data.get("includeLogo", False)
        title = data.get("title", "Reporte de Pago")
        include_payment_details = data.get("includePaymentDetails", True)
        include_user_info = data.get("includeUserInfo", False)
        theme = data.get("theme", "LIGHT")
        include_timestamp = data.get("includeTimestamp", True)
        footer_message = data.get("footerMessage", "Gracias por su pago")
        format = data.get("format", "A4")

        # Crear el reporte usando el Builder
        builder = ReportBuilder()
        builder.set_include_logo(include_logo)
        builder.set_title(title)
        builder.set_include_payment_details(include_payment_details)
        builder.set_include_user_info(include_user_info)
        builder.set_theme(theme)
        builder.set_include_timestamp(include_timestamp)
        builder.set_footer_message(footer_message)
        builder.set_format(format)

        report = builder.build()

        # Generar el PDF
        pdf_content = report.generate_pdf(resultado, monto, tipo)

        # Enviar el PDF como respuesta
        pdf_stream = io.BytesIO(pdf_content)
        pdf_stream.seek(0)
        return send_file(pdf_stream, as_attachment=True, download_name="reporte_pago.pdf", mimetype="application/pdf")

    except Exception as e:
        # Manejo de errores
        print(f"Error al generar el reporte: {str(e)}")  # Agregar registro para depuración
        return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500