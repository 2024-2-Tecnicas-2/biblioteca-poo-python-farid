import sys
import os
import unittest

from src.libro import Libro

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestLibro(unittest.TestCase):
    def test_mostrar_info(self):
        libro = Libro("El libro", 2022, "Autor Desconocido", 100)
        self.assertEqual(libro.mostrar_info(), "El título es: El libro | Año de publicación: 2022 | Autor: Autor Desconocido | Número de páginas: 100")
        
if __name__ == '__main__':
    unittest.main()
