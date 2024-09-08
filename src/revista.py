from src import publicacion

class Revista(publicacion):
    def __init__(self, titulo, year_publicacion, numero_revista, nombre_revista):
        super().__init__(titulo, year_publicacion)
        self.numero_revista = numero_revista
        self.nombre_revista = nombre_revista

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Número de revista: {self.numero_revista} | Nombre de la revista: {self.nombre_revista}"
