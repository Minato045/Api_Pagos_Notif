from interfaces import TemaFactory

class TemaClaro(TemaFactory):
    def crear_header(self):
        return "<header style='background: #eee;'>Tema Claro - Encabezado</header>"

    def crear_footer(self):
        return "<footer style='background: #eee;'>Tema Claro - Pie de página</footer>"

class TemaOscuro(TemaFactory):
    def crear_header(self):
        return "<header style='background: #333; color: white;'>Tema Oscuro - Encabezado</header>"

    def crear_footer(self):
        return "<footer style='background: #333; color: white;'>Tema Oscuro - Pie de página</footer>"