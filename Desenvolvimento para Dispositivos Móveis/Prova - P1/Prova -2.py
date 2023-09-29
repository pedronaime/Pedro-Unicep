def criar_lista():
    lista = []
    for i in range(1, 1001):
        lista.append(float(i)/float(i+1))
    return lista

def somar_valores_da_lista(lista):
    minha_soma: float = 0
    for i in lista:
        minha_soma += i
    return minha_soma


soma = somar_valores_da_lista(criar_lista())

print("A soma dos valores das frações é ", soma)
