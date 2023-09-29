def verificar (p1):
    if p1 > 0:
        return f"O número {p1} é Positivo"
    elif p1 < 0:
        return f"O número {p1} é Negativo"
    else:
        return f"O número {p1} é Neutro"

number = int(input("Digite um nº: "))
resultado = verificar(number)
print(resultado)
