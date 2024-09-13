class Equipment:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name}: Цена - {self.price}, Вес - {self.weight}"
