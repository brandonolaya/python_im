class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._condition = "repose"
        self._engine = Engine(cylinders=4)

    def speed_up(self, type1='slowly'):
        if type1 == 'quick':
            self._engine.inject_gasoline(10)
        else:
            self._engine.inject_gasoline(50)

class Engine:
    def __init__(self, cylinders, type1='gasoline'):
        self.cylinders = cylinders
        self.type = type1
        self._temperature = 0

    def inject_gasoline(self, amount):
        pass