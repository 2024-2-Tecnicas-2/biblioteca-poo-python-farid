from src.libro import Libro
from src.revista import Revista


class Principal:
    def main(self):
     
        libro1 = Libro("El señor de los anillos", 2020, "KL Leonor", 500)
        print(libro1.mostrar_info())
       
        revista1 = Revista("Alquimista", 2021, 65, "Forbes")
        print(revista1.mostrar_info())

if __name__ == "__main__":
    principal = Principal()
    principal.main()
