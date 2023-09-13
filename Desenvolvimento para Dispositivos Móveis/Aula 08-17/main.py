def laptop_discount():

    laptop = 5000
    disconto = 0.9
    acrescimo = 1.1

    forma_de_pagamento = input("Digite (V) para pagar a vista ou (P) para pagar a prazo")

    if forma_de_pagamento == "V":

        laptop *= disconto

    elif forma_de_pagamento == "P":

        laptop *= acrescimo

    print(f"O valor final do laptop com essa forma de pagamento ficou em R$: {laptop:.2f}")


def salary():

    vezes = int(input("Digite a quantidade de vezes que você quer calcular o disconto de um dado salário"))

    for i in range(vezes):

        salario = float(input("Digite o valor do seu salário"))

        if salario >= 5000:

            inss = salario * 0.11
            ir = (salario - inss) * 0.275
            liquido = salario - ir - inss
            print(f"O sálario bruto é de R$: {salario}")
            print(f"O desconto do inss é de R$: {inss}")
            print(f"O desconto do ir é de R$: {ir}")
            print(f"O sálario liquido é de R$: {liquido}")

        else:

            inss = salario * 0.08
            ir = (salario - inss) * 0.225
            liquido = salario - ir - inss
            print(f"O sálario bruto é de R$: {salario}")
            print(f"O desconto do inss é de R$: {inss}")
            print(f"O desconto do ir é de R$: {ir}")
            print(f"O sálario liquido é de R$: {liquido}")


