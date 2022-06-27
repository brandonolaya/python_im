from operator import le
import random

def merge_sort(lista):
    if len(lista) > 1:
        half = len(lista) // 2
        left = lista[:half]
        right = lista[half:]
        print(left, '*' * 5, right)

        # llamada recursiva en cada mitad
        merge_sort(left)
        merge_sort(right)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k +=1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
        
        print(f'izquierda {left}, derecha {right}')
        print(lista)
        print('-' * 50)

    return lista


if __name__ == '__main__':
    list_size = int(input('How big will the list be? '))

    lista = [random.randint(0,100) for i in range(list_size)]
    print(lista)
    print('_' * 10)

    ordered_list = merge_sort(lista)
    print(ordered_list)