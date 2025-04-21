from interfaces import Pago

class PagoCreditCard(Pago):
    def procesar_pago(self, monto):
        return f"Pago de ${monto} procesado con tarjeta de crédito."

class PagoDebitCard(Pago):
    def procesar_pago(self, monto):
        return f"Pago de ${monto} procesado con tarjeta débito."

class PagoPaypal(Pago):
    def procesar_pago(self, monto):
        return f"Pago de ${monto} procesado con PayPal."