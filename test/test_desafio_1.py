import unittest
from src.desafio_1 import escada_string


class TestDesafio1(unittest.TestCase):
    def setUp(self) -> None:
        self.escada_str = escada_string(3)

    def test_escada(self):
        escada_linhas = self.escada_str.splitlines()
        for esperado, atual in enumerate(escada_linhas):
            self.assertEqual(atual.count("*"), esperado + 1)
        self.assertEqual(escada_linhas[-1].strip().count(" "), 0)
