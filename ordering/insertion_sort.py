import random

def insertion_sort(lista):

    for indice in range(1, len(lista)):
        current_value = lista[indice]
        current_position = indice

        while current_position > 0 and lista[current_position - 1] > current_value:
            lista[current_position] = lista[current_position - 1]
            current_position -= 1

        lista[current_position] = current_value
    return lista

if __name__ == '__main__':
    list_size = int(input('How big will the list be? '))

    lista = [random.randint(0,100) for i in range(list_size)]
    print(lista)

    ordered_list = insertion_sort(lista)
    print(ordered_list)