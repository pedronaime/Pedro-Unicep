class Montadora:
    cor = ""
    tipoComb = ""
    velocidade = ""
    qtdPassageiros = ""
    capacTanque = ""

objeto_1 = Montadora()
objeto_2 = Montadora()

objeto_1.cor = "preta"
objeto_1.tipoComb = "flex"
objeto_1.velocidade = 0.0
objeto_1.qtdPassageiros = 5
objeto_1.capacTanque = 42

objeto_2.tipoComb = "disel"

print(objeto_2.tipoComb, objeto_1.qtdPassageiros)