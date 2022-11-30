import unittest

from Imc import Peso_ideal
class TestPeso_ideal(unittest.TestCase):

    def test_peso(self):
        pesocrianca = Peso_ideal("nome", "f", 5, 20, 50)
        valor_esperado = 19
        valor_real = pesocrianca.peso_crianca()
        self.assertEquals(valor_real, valor_esperado)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)