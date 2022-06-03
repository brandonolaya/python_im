def read():
    numbers = []
    with open("./archivos/numbbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Brandon', 'Odin', 'Thor','Afropita', 'Edwin', 'Frank', 'Hulk']
    with open("./archivos/name.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def append():
    names=['Batman', 'SuperTroll']
    with open('./archivos/name.txt', 'a', encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    read()
    write()
    append()

if __name__ == '__main__':
    run()