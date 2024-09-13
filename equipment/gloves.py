from .equipment import Equipment


class Gloves(Equipment):
    def __init__(self, name, price, weight, type):
        super().__init__(name, price, weight)
        self.type = type

    def __str__(self):
        return f"{super().__str__()}, Тип - {self.type}"
