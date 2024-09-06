""" 
Создать классы на основании приведенных ниже спецификаций. Определить конструкторы и соответствующие методы (геттеры — getters и сеттеры — setter) setTun(), getTun(). 
Переопределить методы toString() и hashCode() с целью дальнейшего сравнения нескольких объектов класса. Определить дополнительно методы в классе, создающем массив объектов.
Задать критерий выбора данных и вывести эти данные на консоль. В каждом классе, обладающем информацией, должно быть объявлено несколько конструкторов.

Product: id, Наименование, UPC, Производитель, Цена, Срок хранения, Количество.
Создать массив объектов. Вывести:

a) список товаров для заданного наименования;
b) список товаров для заданного наименования, цена которых не превосходит заданную;
c) список товаров, срок хранения которых больше заданного.
"""

from typing import List


class Product:
    def __init__(self, id, name, upc, manufacturer, price, shelf_life, quantity):
        self._id = id
        self._name = name
        self._upc = upc
        self._manufacturer = manufacturer
        self._price = price
        self._shelf_life = shelf_life
        self._quantity = quantity

    # Геттеры и сеттеры
    def get_id(self): return self._id
    def set_id(self, id): self._id = id

    def get_name(self): return self._name
    def set_name(self, name): self._name = name

    def get_upc(self): return self._upc
    def set_upc(self, upc): self._upc = upc

    def get_manufacturer(self): return self._manufacturer
    def set_manufacturer(self, manufacturer): self._manufacturer = manufacturer

    def get_price(self): return self._price
    def set_price(self, price): self._price = price

    def get_shelf_life(self): return self._shelf_life
    def set_shelf_life(self, shelf_life): self._shelf_life = shelf_life

    def get_quantity(self): return self._quantity
    def set_quantity(self, quantity): self._quantity = quantity

    def __str__(self):
        return f"Product(id={self._id}, name={self._name}, price={self._price}, shelf_life={self._shelf_life})"

    def __hash__(self):
        return hash((self._id, self._name, self._upc, self._manufacturer, self._price, self._shelf_life, self._quantity))


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products_by_name(self, name):
        return [p for p in self.products if p.get_name() == name]

    def get_products_by_name_and_max_price(self, name, max_price):
        return [p for p in self.products if p.get_name() == name and p.get_price() <= max_price]

    def get_products_by_min_shelf_life(self, min_shelf_life):
        return [p for p in self.products if p.get_shelf_life() > min_shelf_life]


# Пример использования
if __name__ == "__main__":
    manager = ProductManager()

    # Создание нескольких продуктов
    products = [Product(1, "Молоко", "123456",
                        "Производитель А", 50.0, 7, 100), Product(2, "Хлеб", "234567", "Производитель Б", 30.0, 3, 50), Product(3, "Молоко", "345678", "Производитель В", 55.0, 10, 80), Product(4, "Вода газированная", "986421", "Производитель Г", 25.0, 14, 150), Product(5, "Сыр", "567890", "Производитель Д", 120.0, 30, 30)]

    # Добавление продуктов в менеджер
    for prod in products:
        manager.add_product(prod)

    # Вывод результатов
    print("Список товаров с наименованием 'Молоко':")
    for product in manager.get_products_by_name("Молоко"):
        print(product)

    print("\nСписок товаров с наименованием 'Молоко' и ценой не выше 52.0:")
    for product in manager.get_products_by_name_and_max_price("Молоко", 52.0):
        print(product)

    print("\nСписок товаров со сроком хранения больше 5 дней:")
    for product in manager.get_products_by_min_shelf_life(5):
        print(product)
