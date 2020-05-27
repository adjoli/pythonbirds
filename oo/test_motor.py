from unittest import TestCase
from carro import Motor

class MotorTestCase(TestCase):
    def test_velocidade(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)
        motor.acelerar()
        self.assertEqual(3, motor.velocidade)
        motor.frear()
        self.assertEqual(1, motor.velocidade)
        motor.frear()
        self.assertEqual(0, motor.velocidade)
