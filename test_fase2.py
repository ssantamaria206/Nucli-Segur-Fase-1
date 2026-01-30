import unittest
from future_motors import Vehicle, Esportiu, Camio

class TestFase2(unittest.TestCase):
    def test_abstracta(self):
        # Intentem crear un Vehicle genèric
        try:
            v = Vehicle("0000", "Test", 0)
            self.fail("Vehicle hauria de ser abstracte!")
        except TypeError:
            pass # Correcte

    def test_preu_esportiu(self):
        ferrari = Esportiu("1111-RED", "Ferrari", 1000)
        # 3 dies * 100€ = 300€
        self.assertEqual(ferrari.calcular_preu(3), 300)

    def test_preu_camio(self):
        volvo = Camio("2222-BIG", "Volvo", 50000, tones=10)
        # (2 dies * 50) + (10 tones * 20) = 100 + 200 = 300€
        self.assertEqual(volvo.calcular_preu(2), 300)

if __name__ == '__main__':
    unittest.main()
