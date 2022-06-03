def run(serie):
    anterior = 0
    actual = 1
    temporal = 0
    
    for i in range(serie):
        temporal = actual
        actual += anterior
        anterior = temporal
        print(f' hay {actual}')
if __name__ == '__main__':
    run(int(input(f'Write and series: ')))