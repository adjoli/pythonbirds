"""
Voce deve criar uma classe carro que vai possuir dois
atributos compostos por outras duas classes:
  1) Motor
  2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
  * Atributo de dado velocidade
  * Método acelerar, aumenta a velocidade de uma unidade
  * Método frear, decrementa a velocidade de duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
  * Valores possíveis: Norte / Sul / Leste / Oeste
  * Método girar à direita
  * Método girar à esquerda

           N
        O     L
           S

  Exemplo:
  >>> # Testando Motor
  >>> motor = Motor()
  >>> motor.velocidade
  0
  >>> motor.acelerar()
  >>> motor.velocidade
  1
  >>> motor.acelerar()
  >>> motor.velocidade
  2
 >>> motor.acelerar()
  >>> motor.velocidade
  3
  >>> motor.frear()
  >>> motor.velocidade
  1
  >>> motor.frear()
  >>> motor.velocidade
  0
  >>> # Testando Direção
  >>> direcao = Direcao()
  >>> direcao.valor
  'Norte'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Leste'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Sul'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Oeste'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Norte'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Oeste'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Sul'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Leste'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Norte'
  >>> # Testando Carro
  >>> carro = Carro(motor, direcao)
  >>> carro.calcular_velocidade()
  0
  >>> carro.acelerar()
  >>> carro.calcular_velocidade()
  1
  >>> carro.acelerar()
  >>> carro.calcular_velocidade()
  2
  >>> carro.frear()
  >>> carro.calcular_velocidade()
  0
  >>> carro.calcular_direcao()
  'Norte'
  >>> carro.girar_a_direita()
  >>> carro.calcular_direcao()
  'Leste'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao()
  'Norte'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao()
  'Oeste'
"""


# ------------------------------------------------------------------
class Motor:
    def __init__(self):
        self.velocidade = 0

    @property
    def velocidade(self):
        return self._velocidade

    @velocidade.setter
    def velocidade(self, vel):
        # Se velocidade for negativa, velocidade recebe 0
        self._velocidade = max(0, vel)

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2


# ------------------------------------------------------------------
class Direcao:
    _valores = ('Norte', 'Leste', 'Sul', 'Oeste')

    def __init__(self):
        self._cursor = 0

    @property
    def valor(self):
        return self._valores[self._cursor]

    def girar_a_direita(self):
        self._cursor = (self._cursor + 1) % len(self._valores)

    def girar_a_esquerda(self):
        self._cursor = (self._cursor - 1) % len(self._valores)


# ------------------------------------------------------------------

class Carro:
    """Implementacao da classe Carro, e suas classe agregadas Motor e Direcao"""
    def __init__(self, motor, direcao):
        self._motor = motor
        self._direcao = direcao

    def calcular_velocidade(self):
        return self._motor.velocidade

    def acelerar(self):
        self._motor.acelerar()

    def frear(self):
        self._motor.frear()

    def calcular_direcao(self):
        return self._direcao.valor

    def girar_a_direita(self):
        self._direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self._direcao.girar_a_esquerda()
