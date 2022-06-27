import random, time

def binary_search(listt, start, final, focus):
    #para saber donde estamos buscando
    print(f'buscando {focus} entre {listt[start]} y {listt[final - 1]}')
    #compara el inicio y final de la lista 
    if start > final:
        return False
    #parte la lista a la mitad
    half = (start + final) // 2

    # hace las comparaciones
    if listt[half] == focus:
        return True
    elif listt[half] < focus:
        return binary_search(listt, half + 1 , final, focus)
    else:
        return binary_search(listt, start, half -1, focus)

if __name__ == '__main__':
    list_size = int(input('What is the size of the list? '))
    focus= int(input('What number do you want to find? '))
    
    listt = sorted([random.randint(0,1000) for i in range(list_size)])
    comienzo = time.time()
    encontrado = binary_search(listt, 0, len(listt), focus)
    
    #print(listt)
    print(f'El elemento {focus} {"esta" if encontrado else "no esta"} en la lista')
    final = time.time()
    print(final - comienzo)