from unittest import TestCase
from carro import Direcao

class DirecaoTestCase(TestCase):
    def test_direcao(self):
        direcao = Direcao()
        direcao.valor

        # Testando girar_a_direita
        self.assertEqual('Norte', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Leste', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Sul', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Oeste', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Norte', direcao.valor)

        # Testando girar_a_esquerda
        direcao.girar_a_esquerda()
        self.assertEqual('Oeste', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Sul', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Leste', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Norte', direcao.valor)
