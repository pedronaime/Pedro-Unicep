class Montadora2:
    def __init__(self, p1, p2, p3, p4, p5):
        self.cor = p1
        self.tipoComb = p2
        self.velocidade = p3
        self.qtdPassageiros = p4
        self.capacTanque = p5


objeto_1 = Montadora2("preta", "flex", 0.0, 5, 42)
objeto_2 = Montadora2("branca", "disel", 0.0, 6, 60)

print(objeto_2.tipoComb, objeto_1.qtdPassageiros)