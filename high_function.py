#palindromo = lambda string: string == string[::-1]

def palindromo(string):
    return string == string[::-1]

print(palindromo('ana'))

def saludo(func):
    func()

def hola():
    print("Hola hijos de puta")

def adios():
    print("Adios hijos de puta")

saludo(hola)
saludo(adios)