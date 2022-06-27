import random

def linear_search(listt, focus):
    match = False

    for element in listt: #O(n)
        if element == focus:
            match = True
            break
    return match

if __name__ == '__main__':
    list_size = int(input('What is the size of the list? '))
    focus= int(input('What number do you want to find? '))
    
    listt = [random.randint(0,100) for i in range(list_size)]
    
    encontrado = linear_search(listt, focus)
    
    print(listt)
    print(f'El elemento {focus} {"esta" if encontrado else "no esta"} en la lista')