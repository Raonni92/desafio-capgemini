import unittest

from src.desafio_2 import verificar_senha_forte


class TestSenhaForte(unittest.TestCase):
    def test_senha_sem_minuscula(self):
        senha = "A#1BBV"
        self.assertEqual(verificar_senha_forte(senha), 1)

    def test_senha_sem_maiuscula(self):
        senha = "a#1bbv"
        self.assertEqual(verificar_senha_forte(senha), 1)

    def test_senha_sem_digito(self):
        senha = "a#@Bbv"
        self.assertEqual(verificar_senha_forte(senha), 1)

    def test_senha_sem_especial(self):
        senha = "a12Bbv"
        self.assertEqual(verificar_senha_forte(senha), 1)

    def test_senha_sem_tamanho_minimo(self):
        senha = "a#@Bb"
        self.assertEqual(verificar_senha_forte(senha), 1)

    def test_senha_faltando_mais_regra_tamanho(self):
        senha = "a#@bb123"
        self.assertEqual(verificar_senha_forte(senha), 1)
