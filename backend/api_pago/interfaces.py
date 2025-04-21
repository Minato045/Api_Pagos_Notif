from abc import ABC, abstractmethod

class Pago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass