class Employee:
    raise_amt= 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.12

    def __init__(self, first, last, pay, program_language):
        super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay)
        self.program_language = program_language


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


if __name__ == '__main__':
    dev_1 = Developer('Brandon', 'Olaya', 50000, 'Python')
    dev_2 = Developer('Ivan', 'Lokita', 30000, 'Java')
    
    mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
    print(mgr_1.email)
    mgr_1.print_emps()