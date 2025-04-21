from abc import ABC, abstractmethod

class TemaFactory(ABC):
    @abstractmethod
    def crear_header(self): pass

    @abstractmethod
    def crear_footer(self): pass