def soma(a,b):
    x = a + b
    print(f"soma = {x}")


def soma_r(a,b):
    x = a + b
    return x


def maior(a,b):

    if a > b:
        return a
    else:
        return b


def maiorMenor(a,b):

    if a > b:
        return a,b
    else:
        return b,a


x,y = maiorMenor(100,15)


# definicao de tupla => tupla = (1,2,3) (lista constante)
# definicao de lista => lista = [1,2,3] (lista normal)



# essa função recebe quantos argumentos quiser
def test(*argumentos):
    for elemento in argumentos:
        print(elemento)


def divisores(n):
    lista = []
    i = 1
    while i<=n:
        resto = n % i
        if resto == 0:
            lista.append(i)

        i=i+1

    return lista

x = divisores(9)
for elemento in x:
    print(elemento)




