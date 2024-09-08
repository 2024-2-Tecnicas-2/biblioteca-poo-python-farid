from src import publicacion

class Libro(publicacion):
    def __init__(self, titulo, year_publicacion, autor, numero_paginas):
        super().__init__(titulo, year_publicacion)
        self.autor = autor
        self.numero_paginas = numero_paginas

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Autor: {self.autor} | Número de páginas: {self.numero_paginas}"
