# shopping_list.py

# Инициализация пустого списка покупок (словаря)
shopping_list = {}

# Добавление элемента в список
def add_item(item_name, quantity=0):
    if item_name in shopping_list:
        shopping_list[item_name] += quantity  # Если объект уже есть, увеличиваем количество
    else:
        shopping_list[item_name] = quantity  # Если объекта нет, добавляем новый

# Удаление элемента из списка
def remove_item(item_name):
    if item_name in shopping_list:
        del shopping_list[item_name]  # Удаляем элемент из словаря
    else:
        print(f"'{item_name}' нет в списке.")

# Редактирование количества элемента
def edit_quantity(item_name, quantity):
    if item_name in shopping_list:
        shopping_list[item_name] = quantity  # Изменяем количество
    else:
        print(f"'{item_name}' нет в списке. Сначала добавьте его.")

# Просмотр всего списка покупок
def view_list():
    if shopping_list:
        print("\nСписок покупок:")
        for item, quantity in shopping_list.items():
            print(f"- {item}: {quantity}")
    else:
        print("\nСписок покупок пуст.")
