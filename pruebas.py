import unittest
import libreriacomplejos as cplxlib
class TestCplxMethods(unittest.TestCase):

    def test_suma(self):
        c1 = (5.6, -8.9)
        c2 = (-3.4, 6.2)
        c3 = (-7.4, 3.2)
        c4 = (8.6, 7.1)
        self.assertAlmostEqual(cplxlib.suma(c1, c2)[0], 2.2)
        self.assertAlmostEqual(cplxlib.suma(c1, c2)[1], -2.7)
        self.assertAlmostEqual(cplxlib.suma(c3, c4)[0], 1.2)
        self.assertAlmostEqual(cplxlib.suma(c3, c4)[1], 10.3)

    def test_resta(self):
        c1=(3,8)
        c2=(7,4)
        c3 = (3, 3.2)
        c4 = (20.1, 3.4)
        self.assertAlmostEqual(cplxlib.resta(c1, c2)[0], -4)
        self.assertAlmostEqual(cplxlib.resta(c1, c2)[1], 4)
        self.assertAlmostEqual(cplxlib.resta(c3, c4)[0], -17.1)
        self.assertAlmostEqual(cplxlib.resta(c3, c4)[1], -0.2)

    def test_mult(self):
        c1 = (5.6, -8.9)
        c2=(7,4)
        c3 = (3, 1.5)
        c4=(4.3,9.2)
        self.assertAlmostEqual(cplxlib.producto(c1, c2)[0], 74.8)
        self.assertAlmostEqual(cplxlib.producto(c1, c2)[1], -39.9)
        self.assertAlmostEqual(cplxlib.producto(c3, c4)[0], -0.9)
        self.assertAlmostEqual(cplxlib.producto(c3, c4)[1], 34.05)

    def test_div(self):
        c1=(1,1)
        c2=(4,3)
        c3 = (3, 1.5)
        c4=(4.3,9.2)
        self.assertAlmostEqual(cplxlib.division(c1, c2)[0], 0.4375)
        self.assertAlmostEqual(cplxlib.division(c1, c2)[1], 0..04)
        self.assertAlmostEqual(cplxlib.division(c3, c4)[0], 1.44)
        self.assertAlmostEqual(cplxlib.division(c3, c4)[1], -0.2)

    def test_mod(self):
        c1=(1,1)
        c2=(4,3)
        self.assertAlmostEqual(cplxlib.modulo(c1), 1.41)
        self.assertAlmostEqual(cplxlib.modulo(c2), 5)

    def test_conjugada(self):
        c1=(4,2)
        c2=(3,1)
        self.assertAlmostEqual(cplxlib.conjugado(c1)[0], 4)
        self.assertAlmostEqual(cplxlib.conjugado(c1)[2], -2)
        self.assertAlmostEqual(cplxlib.conjugado(c1)[0], 3)
        self.assertAlmostEqual(cplxlib.conjugado(c1)[2], -1)

    def test_polar(self):
        c1=(7,2)
        c2=(3.8,5.9)
        self.assertAlmostEqual(cplxlib.polar(c1)[0], 7.28)
        self.assertAlmostEqual(cplxlib.polar(c1)[1], 0.27)
        self.assertAlmostEqual(cplxlib.polar(c2)[0], 7.01)
        self.assertAlmostEqual(cplxlib.polar(c2)[1], 0.99)

    def test_rectangular(self):
        c1=(4,65)
        c2=(7.8,102)
        self.assertAlmostEqual(cplxlib.rectangular(c1)[0], -2.249)
        self.assertAlmostEqual(cplxlib.rectangular(c1)[1], 3.307)
        self.assertAlmostEqual(cplxlib.rectangular(c2)[0], 0.7923)
        self.assertAlmostEqual(cplxlib.rectangular(c2)[1], 7.7596)

    def fase(self):
        c1=(7,2)
        c2=(3.8,5.9)
        self.assertAlmostEqual(cplxlib.fase(c1), 0.27)
        self.assertAlmostEqual(cplxlib.suma(c2), 0.998)

    if __name__ == '__main__':
        unittest.main()