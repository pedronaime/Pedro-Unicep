class Funcionario:
    def __init__(self, nome, tempo_de_casa, salario):
        self.m_nome = nome
        self.m_tempo_de_casa = tempo_de_casa
        self.m_salario = salario

    def aumento_de_salario(self):
        if self.m_tempo_de_casa < 10:
            self.m_salario *= 1.05
        else:
            self.m_salario *= 1.1

    def impressao(self):
        print(f"O funcionário {self.m_nome} tem "
              f"{self.m_tempo_de_casa} anos de casa "
              f"e um sálario de {self.m_salario}")


funcionario_1 = Funcionario("Alberto", 5, 1000)
funcionario_2 = Funcionario("Maria", 15, 5000)
funcionario_1.impressao()
funcionario_1.aumento_de_salario()
funcionario_1.impressao()
funcionario_2.impressao()
funcionario_2.aumento_de_salario()
funcionario_2.impressao()