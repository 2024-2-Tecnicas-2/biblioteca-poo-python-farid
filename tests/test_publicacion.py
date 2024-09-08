import sys
import os
import unittest



# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestPublicacion(unittest.TestCase):
  class TestPublicacion(unittest.TestCase):
    def test_mostrar_info(self):
        publicacion = publicacion("Prueba", 2022)
        self.assertEqual(publicacion.mostrar_info(), "El título es: Prueba | Año de publicación: 2022")

        
if __name__ == '__main__':
    unittest.main()
