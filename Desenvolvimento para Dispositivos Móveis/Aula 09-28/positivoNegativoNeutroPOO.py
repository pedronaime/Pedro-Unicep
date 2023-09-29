class PositivoNegativoNeutroPOO:
    def __init__(self, p1):
        self.number = p1

    def verificar(self):
        if self.number > 0:
            return f"O número {self.number} é Positivo"
        elif self.number < 0:
            return f"O número {self.number} é Negativo"
        else:
            return f"O número {self.number} é Neutro"


numero = int(input("Digite um nº: "))
resultado = PositivoNegativoNeutroPOO(numero)
print(resultado.verificar())