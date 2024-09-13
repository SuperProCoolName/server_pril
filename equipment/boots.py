from .equipment import Equipment


class Boots(Equipment):
    def __init__(self, name, price, weight, size):
        super().__init__(name, price, weight)
        self.size = size

    def __str__(self):
        return f"{super().__str__()}, Размер - {self.size}"
