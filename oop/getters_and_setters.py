class Employee:
    def __init__(self, first, last):
        """Declaro los contructores first, last,emagil
        """
        self.first = first
        #tendra un problemas el cual no se cambio el nombre        
        #self.email = first + '.' + last + '@email.com'
        self.last = last

    #para cuando lo llamemeos no tenga que tener los () esto es la decoracion
    @property
    def email(self):
        """Solicionamos el problemas por que no cambiaba el nombre al email
        """
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        """Devuelve el resultador del nombre y apellido
        """
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!!')
        self.first = None
        self.last = None

emp_1 = Employee('Brandon', 'Olaya')
emp_1.first = 'Kranditon'
#mato los ateriores 
emp_1.fullname = 'Brad Olaf'


print(emp_1.first)
#print(emp_1.fullname())
#print(emp_1.email())
print(emp_1.email)
del emp_1.fullname
print(emp_1.fullname)

