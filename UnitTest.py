import unittest
from Examen2 import MiClase


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7], [1, 2, 3])

    def testObtieneValencia1(self):
        resultado = self.objeto.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)

    def testObtieneValencia2(self):
        resultado = self.objeto.ObtieneValencia(24680)
        self.assertEqual(resultado, 0)

    def testDivisibleTempo1(self):
        resultado = self.objeto.DivisibleTempo(2)
        self.assertEqual(resultado, [1, 2])

    def testDivisibleTempo2(self):
        resultado = self.objeto.DivisibleTempo(0)
        self.assertEqual(resultado, [])

    def testObtieneMasBailable1(self):
        resultado = self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7])
        self.assertEqual(resultado, 0.9)

    def testObtieneMasBailable2(self):
        resultado = self.objeto.ObtieneMasBailable([])
        self.assertIsNone(resultado)

    def testVerificaListaCanciones1(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"])
        self.assertTrue(resultado)

    def testVerificaListaCanciones2(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", None])
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
