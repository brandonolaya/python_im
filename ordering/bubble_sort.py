import random

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1]= lista[j + 1], lista[j]
    return lista

if __name__ == '__main__':
    list_size = int(input('How big will the list be? '))

    lista = [random.randint(0,100) for i in range(list_size)]
    print(lista)

    ordered_list = bubble_sort(lista)
    print(ordered_list)