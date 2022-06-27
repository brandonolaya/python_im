class Person:

    def __init__(self, name):
        self.name=name

    def walk(self):
        print('I am walking')


class Run(Person):
    """herncia copy
        polimordismo edit
    """
    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        print('I am runing with my dog')


def main():
    personita = Person('Brandon')
    personita.walk()

    corredor = Run('Brenda')
    corredor.walk()


if __name__ == '__main__':
    main()