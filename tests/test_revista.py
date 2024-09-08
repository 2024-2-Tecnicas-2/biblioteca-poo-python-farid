import sys
import os
import unittest

from src.revista import Revista

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestRevista(unittest.TestCase):
   class TestRevista(unittest.TestCase):
    def test_mostrar_info(self):
        revista = Revista("Revista", 2021, 10, "Ciencia Hoy")
        self.assertEqual(revista.mostrar_info(), "El título es: Revista | Año de publicación: 2021 | Número de revista: 10 | Nombre de la revista: Ciencia Hoy")
        
if __name__ == '__main__':
    unittest.main()
