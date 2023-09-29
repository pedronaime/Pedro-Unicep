class ParImparPOO:
    def __init__(self, p1):
        self.number = p1

    def verificar(self):
        if self.number % 2 == 0:
            return f"{self.number} é par"
        else:
            return f"{self.number} é impar"


number = int(input("Digite um nº "))
objeto_1 = ParImparPOO(number)
objeto_2 = ParImparPOO(11)
resultado_1 = objeto_1.verificar()
resultado_2 = objeto_2.verificar()
print(resultado_1)
print(resultado_2)
