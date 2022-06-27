import re


class Persona():

    def __init__(self, first_name, last_name):
        """creo el constructor
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def fullname(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Estudiante(Persona):
    
    def __init__(self, first_name, last_name, profesion):
        super().__init__(first_name, last_name)
        self.profesion = profesion


class Nota(Estudiante):
    def __init__(self, first_name, last_name, profesion, notas):
        super().__init__(first_name, last_name, profesion)
        self.notas = notas
    


if __name__ == '__main__':
    estu_1 = Nota('Brandon', 'Olaya', 'programador' , 2)
    print(estu_1.profesion)
    print(estu_1.notas)
    print(estu_1.promedio)