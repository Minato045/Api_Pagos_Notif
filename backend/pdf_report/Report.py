from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
import datetime
import io
import os

class Report:
    def __init__(self, include_logo, title, include_payment_details, include_user_info, theme, include_timestamp, footer_message, format):
        self.include_logo = include_logo
        self.title = title
        self.include_payment_details = include_payment_details
        self.include_user_info = include_user_info
        self.theme = theme
        self.include_timestamp = include_timestamp
        self.footer_message = footer_message
        self.format = format

    def generate_pdf(self, resultado, monto, tipo):
        try:
            buffer = io.BytesIO()
            page_size = A4 if self.format == "A4" else letter
            pdf = canvas.Canvas(buffer, pagesize=page_size)

            # Tema de colores
            if self.theme == "DARK":
                pdf.setFillColorRGB(1, 1, 1)  # Texto blanco para fondo oscuro
                pdf.setStrokeColorRGB(1, 1, 1)
            else:
                pdf.setFillColorRGB(0, 0, 0)  # Texto negro para fondo claro
                pdf.setStrokeColorRGB(0, 0, 0)

            # Título
            pdf.setFont("Helvetica-Bold", 16)
            pdf.drawString(100, 750, self.title)

            # Logo
            if self.include_logo:
                logo_path = os.path.join("public", "logo.png")
                if os.path.exists(logo_path):
                    x = (page_size[0] - 100) / 2  # Centrar horizontalmente
                    y = 700  # Mantener la posición vertical
                    pdf.drawImage(logo_path, x, y, width=100, height=100)
                else:
                    pdf.drawString(50, 700, "Logo no disponible")

            # Detalles del pago
            if self.include_payment_details:
                pdf.setFont("Helvetica", 12)
                pdf.drawString(50, 650, f"Resultado del Pago: {resultado}")
                pdf.drawString(50, 630, f"Monto: ${monto}")
                pdf.drawString(50, 610, f"Tipo de Pago: {tipo}")

            # Información adicional del usuario
            if self.include_user_info:
                try:
                    pdf.drawString(50, 590, "Información del usuario:")
                    pdf.drawString(50, 570, "Nombre: ***************")
                    pdf.drawString(50, 550, "Correo: ************@gmail.com")
                except Exception as e:
                    pdf.drawString(50, 590, "Error al incluir información del usuario")

            # Timestamp
            if self.include_timestamp:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                pdf.drawString(50, 530, f"Fecha y Hora: {timestamp}")

            # Footer
            pdf.drawString(50, 50, self.footer_message)

            pdf.save()
            buffer.seek(0)
            return buffer.getvalue()

        except Exception as e:
            print(f"Error al generar el PDF: {str(e)}")
            raise