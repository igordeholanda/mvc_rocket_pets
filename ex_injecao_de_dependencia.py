class Motor:
    def ligar(self):
        print("Motor ligado!")

class MotorEletrico:
    def ligar(self):
        print("Motor eletrico ligado!")

class MotorCombustao:
    def ligar(self):
        print("Motor a combustao ligado!")


# O carro precisa de um motor, mas não cria ele sozinho
class Carro:
    def __init__(self, motor1):
        self.motor = motor1  # O motor foi "injetado" no carro

    def dirigir(self):
        self.motor.ligar()
        print("Carro em movimento!")


# Criamos o motor fora do carro e o "injetamos"

motor = Motor()
carro = Carro(motor)
carro.dirigir()
print()

motor_eletrico = MotorEletrico()
carro= Carro(motor_eletrico)
carro.dirigir()
print()

motor_combustao = MotorCombustao()
carro = Carro(motor_combustao)
carro.dirigir()
