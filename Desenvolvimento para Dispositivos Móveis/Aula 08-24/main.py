my_list = []
user_control = 10


def add_number(number):
    if len(my_list) == 5:
        print("A lista não consegue guargar mais nenhum número")
    else:
        my_list.append(number)


def remove_number():
    if len(my_list) <= 0:
        print("Não tem nenhum número na lista para ser removido")
    else:
        my_list.pop()


def list_all_number():
    number_to_print = "Os números na lista são: "
    for i in my_list:
        number_to_print += i + " "

    print(number_to_print)


WHATEVER = 10

while user_control != 0:
    user_control = int(input("1 - Incluir\n2 - Remover\n3 - Listar\n0 - Sair\n"))

    if user_control == 1:
        number_to_include = input("Digite o número para ser incluído: ")
        add_number(number_to_include)
    elif user_control == 2:
        remove_number()
    elif user_control == 3:
        list_all_number()
