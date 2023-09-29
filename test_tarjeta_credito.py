import unittest
from tarjeta import TarjetaCredito

class TestTarjetaCredito(unittest.TestCase):
    def setUp(self):
        self.tarjeta = TarjetaCredito()

    def test_filtrar_digitos(self):
        self.assertEqual(self.tarjeta.filtrar_digitos("a1b2c3d4"), "1234")

    def test_validar_numero(self):
        self.assertTrue(self.tarjeta.validar_numero("1234567890123456"))
        self.assertFalse(self.tarjeta.validar_numero("12345"))

    def test_validar_fecha_expiracion(self):
        self.assertTrue(self.tarjeta.validar_fecha_expiracion("0125"))
        self.assertFalse(self.tarjeta.validar_fecha_expiracion("0115"))

    def test_validar_cvc(self):
        self.assertTrue(self.tarjeta.validar_cvc("123"))
        self.assertFalse(self.tarjeta.validar_cvc("12"))

    def test_verificar_saldo(self):
        self.assertTrue(self.tarjeta.verificar_saldo(100.0))

    def test_validar(self):
        self.assertEqual(self.tarjeta.validar("1234567890123456", "0125", "123", 100.0), "Tarjeta de crédito válida.")
        self.assertEqual(self.tarjeta.validar("12345", "0125", "123", 100.0), "Número de tarjeta inválido.")

if __name__ == "__main__":
    unittest.main()
