from metodos_pago import PagoCreditCard, PagoDebitCard, PagoPaypal

class PagoFactory:
    @staticmethod
    def crear_pago(tipo):
        if tipo == "credit":
            return PagoCreditCard()
        elif tipo == "debit":
            return PagoDebitCard()
        elif tipo == "paypal":
            return PagoPaypal()
        else:
            raise ValueError("Tipo de pago no soportado")