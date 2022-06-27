class Washing_machine:
    def __init__(self) -> None:
        pass
    #variable publica
    def wash(self, temperture='cold'):
        self._fill_water_tank(temperture)
        self._add_soap()
        self._wash()
        self._centrifuge()
    #variable privada
    def _fill_water_tank(self, temperature):
        print(f'Filling the tank with water {temperature}')

    def _add_soap(self):
        print('Add soap')

    def _wash(self):
        print(f'Wash')

    def _centrifuge(self):
        print(f'Centrifuge')

if __name__ == '__main__':
    washing_machine = Washing_machine()
    washing_machine.wash()