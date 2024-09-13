import os
from equipment.helmet import Helmet
from equipment.jacket import Jacket
from equipment.gloves import Gloves
from equipment.boots import Boots


def load_equipment(file_path):
    equipment_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == 'Helmet':
                equipment_list.append(
                    Helmet(data[1], float(data[2]), float(data[3]), data[4]))
            elif data[0] == 'Jacket':
                equipment_list.append(
                    Jacket(data[1], float(data[2]), float(data[3]), data[4]))
            elif data[0] == 'Gloves':
                equipment_list.append(
                    Gloves(data[1], float(data[2]), float(data[3]), data[4]))
            elif data[0] == 'Boots':
                equipment_list.append(
                    Boots(data[1], float(data[2]), float(data[3]), data[4]))
    return equipment_list


def display_equipment(equipment_list):
    for equipment in equipment_list:
        print(equipment)


def calculate_total_cost(equipment_list):
    return sum(equipment.price for equipment in equipment_list)


def sort_equipment_by_weight(equipment_list):
    def get_weight(equipment):
        return equipment.weight

    return sorted(equipment_list, key=get_weight)


def find_equipment_by_price_range(equipment_list, min_price, max_price):
    return [equipment for equipment in equipment_list if min_price <= equipment.price <= max_price]


def main():
    file_path = os.path.join('data', 'equipment_data.txt')
    equipment_list = load_equipment(file_path)

    print("Экипировка мотоциклиста:")
    display_equipment(equipment_list)

    total_cost = calculate_total_cost(equipment_list)
    print(f"\nОбщая стоимость экипировки: {total_cost}")

    sorted_equipment = sort_equipment_by_weight(equipment_list)
    print("\nЭкипировка, отсортированная по весу:")
    display_equipment(sorted_equipment)

    min_price = float(input("\nВведите минимальную цену: "))
    max_price = float(input("Введите максимальную цену: "))
    filtered_equipment = find_equipment_by_price_range(
        equipment_list, min_price, max_price)
    print("\nЭкипировка в заданном диапазоне цен:")
    display_equipment(filtered_equipment)


if __name__ == "__main__":
    main()
