from .equipment import Equipment


class Jacket(Equipment):
    def __init__(self, name, price, weight, material):
        super().__init__(name, price, weight)
        self.material = material

    def __str__(self):
        return f"{super().__str__()}, Материал - {self.material}"
