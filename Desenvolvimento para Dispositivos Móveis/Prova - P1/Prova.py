my_list = []


def inserir(lista, elemento):
    if len(lista) < 3:
        lista.insert(0, elemento)
    else:
        print("Não é possivel inserir um quarto elemento!")


def remover(lista):
    if len(lista) <= 0:
        print("A lista está vazia!")
        return
    lista.pop(len(lista) - 1)


while True:
    ""
    print(" ")
    print("1-Incluir")
    print("2-Retirar")
    print("3-Encerrar")
    ""

    opcao = int(input("Digite uma opção "))

    if opcao == 1:
        numero = int(input("Digite um numero a ser inserido na lista "))
        inserir(my_list, numero)
    elif opcao == 2:
        print("Você removeu o elemento ", my_list[len(my_list) - 1], " da lista")
        remover(my_list)
    elif opcao == 3:
        break
