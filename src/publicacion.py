class publicacion:
    def __init__(self, titulo, year_publicacion):
        self.titulo = titulo
        self.year_publicacion = year_publicacion

    def mostrar_info(self):
        return f"El título es: {self.titulo} | Año de publicación: {self.year_publicacion}"

