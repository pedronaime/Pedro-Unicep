def verificar(p1):
    if p1 % 2 == 0:
        return f"{p1} é par"
    else:
        return f"{p1} é impar"

number = int(input("Digite um nº "))
resultado = verificar(number)
print(resultado)