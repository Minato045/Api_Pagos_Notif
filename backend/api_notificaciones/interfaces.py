from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, *args, **kwargs):  # Permite argumentos variables
        pass