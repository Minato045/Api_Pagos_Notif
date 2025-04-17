from temas import TemaClaro, TemaOscuro

def get_tema_factory(nombre):
    if nombre == "claro":
        return TemaClaro()
    elif nombre == "oscuro":
        return TemaOscuro()
    else:
        raise ValueError("Tema no soportado")